"""
    Realice un programa que le permita calcular el discriminante con raices negativas
"""
import math

a = int(input("Ingrese el valor de A  "))
b = int(input("Ingrese el valor de B  "))
c = int(input("Ingrese el valor de C  "))


def raiz(a, b):
    raiz = math.pow(b, 2) - 4 * a * c
    if raiz >= 0:
        print("\nX1 => ", (-b + math.sqrt(raiz)) / (2 * a),
              "\nX2 => ", (-b - math.sqrt(raiz)) / (2 * a))
    else:
        raiz *= -1
        print("\nX1 => ", (-b + math.sqrt(raiz)) / (2 * a), "i",
              "\nX2 => ", (-b - math.sqrt(raiz)) / (2 * a), "j")


raiz(a, b)
