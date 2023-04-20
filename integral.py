import numpy as np
import matplotlib.pyplot as plt
import sympy
import re

# Función que define la regla del trapecio
def regla_trapecio(a, b, f, n):
    h = (b-a)/n
    x = np.linspace(a,b,n+1)
    y = [f.subs('x', i) for i in x]
    s = sum(y[1:-1])
    return (h/2)*(sympy.expand(y[0]) + sympy.expand(y[-1]) + 2*s)

while True:
    try:
        funcion = input("Introduce la función a integrar: ").strip()
        
        if len(funcion) == 0:
            raise Exception("Error: la entrada de la función no puede estar en blanco. Introduce una función en la forma 'sin(x)'.")

        # Convertir la cadena de la función en un objeto funcional
        x = sympy.symbols('x')

        f = sympy.sympify(funcion) # Convertir la cadena en un objeto SymPy

        # Verificar si la función tiene una singularidad en x=0
        if sympy.limit(f, x, 0) == sympy.oo or sympy.limit(f, x, 0) == -sympy.oo:
            raise Exception("Error: la función tiene una singularidad en x=0. Introduce otra función que se pueda evaluar.")

        a = float(input("Introduce el límite inferior: ").strip())
        b = float(input("Introduce el límite superior: ").strip())
        n = int(input("Introduce el número de subintervalos: ").strip())

        integral = regla_trapecio(a, b, f, n)
        
        print("El resultado de la integración es:", integral)

        # Graficar la función y los puntos
        x = np.linspace(a,b,n+1)
        y = [f.subs('x', i) for i in x]
        plt.plot(x,y,'b')
        plt.plot(x,y,'ro')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Regla del trapecio')

        for i in range(n):
            xs = [x[i], x[i], x[i+1], x[i+1]]
            ys = [0, f.subs('x', x[i]), f.subs('x', x[i+1]), 0]
            plt.fill(xs, ys, '#3AFF00', alpha=0.6)
            
            # Líneas que separan los trapecios
            plt.plot([x[i], x[i]], [0, f.subs('x', x[i])], 'k--')
            plt.plot([x[i+1], x[i+1]], [0, f.subs('x', x[i+1])], 'k--')

        plt.show()

        break
    except Exception as e:
        print(str(e))
