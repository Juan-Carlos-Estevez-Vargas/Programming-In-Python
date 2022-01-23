"""
    Realizar un programa que dado un conjunto d enúmeros cuente cuantos son
    divisibles entre 3, cuentos entre 7 y cuantos entre 3 y 7. Para ello
    debe emplear un bucle while
"""

num = 0
divisibles_tres = 0
divisibles_siete = 0
divisibles_tres_y_siete = 0
contador_numeros = 0

while num < 99:
    num = int(input("Ingrese un número por favor  "))
    if num % 3 == 0:
        divisibles_tres += 1
    elif num % 7 == 0:
        divisibles_siete += 1
    elif num % 3 == 0 and num % 7 == 0:
        divisibles_tres_y_siete += 1
    contador_numeros += 1

print("\nLa cantidad total de números son : ", contador_numeros,
      "\nLa cantidad de números divisibles en 3 son : ", divisibles_tres,
      "\nLa cantidad de números divisibles en 7 son : ", divisibles_siete,
      "\nLa cantidad de números divisibles en 3 y 7 son : ", divisibles_tres_y_siete)