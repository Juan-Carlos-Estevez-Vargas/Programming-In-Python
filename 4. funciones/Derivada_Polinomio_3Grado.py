"""
    Realice un programa que calcule la derivada de un polinomio de 3er grado
"""
a = int(input("Ingrese el valor de A  "))
b = int(input("Ingrese el valor de B  "))
c = int(input("Ingrese el valor de C  "))
d = int(input("Ingrese el valor de D  "))


def derivada(a, b, c, d):
    print("\nExpresión original :  ", a, "x^3   +   ", b, "x^2", c, "x  +   ", d,
          "\nExpresión derivada :  ", a * 3, "x^2   +   ", b * 2, "x    +   ", c)

derivada(a, b, c, d)