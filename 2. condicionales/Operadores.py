a = float(input("Ingrese un número por favor -> "))
b = float(input("Ingrese un segundo número por favor -> "))
print("\nLa división entera entre ambos número es: ", (a//b))
if a > b:
    print("El número ", a, " es mayor que el número ",b)
elif a < b:
    print("El número ", b, " es mayor que el número ",a)
elif a == b:
    print("Ambos números osn iguales")

if a != b:
    print("Los números son distintos")

print("El módulo de la división entre ", a, " y ", b, " es: ", (a%b))