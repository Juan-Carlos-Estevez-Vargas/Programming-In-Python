"""
Determinar el valor total a pagar por una llamada telefónica, de acuerdo a lo siguiente:

    • Toda llamada que dure menos de tres minutos, tiene un costo de $500.
    • Cada minuto adicional‐local a partir de los tres primeros, tiene un costo de $200.
    • Cada minuto adicional‐nacional a partir de los tres primeros, tiene un costo de $300.
"""
def llamadas():
    llamada = int(input("\n--------------------------------------\n"
                        "-    ¿Qué tipo de llamada realizó?   -\n"
                        "--------------------------------------\n"
                        "-    1. LLamada nacional             -\n"
                        "-    2. LLamada internacional        -\n"
                        "--------------------------------------\n"))
    if llamada == 1:
        minutos(1)
    elif llamada == 2:
        minutos(2)
    else:
        print("Ingreso una opción incorrecta, vuelva a intentarlo")
        llamadas()


def minutos(n):
    minutos = int(input("Ingrese la cantidad de minutos que tardó "))

    if minutos < 3:
        print("El valor a pagar es: $", 500)
    elif minutos >= 3 and n == 1:
        print("El valor a pagar es: $", ((minutos - 2) * 300) + 500)
    elif minutos >= 3 and n == 2:
        print("El valor a pagar es: $", ((minutos - 2) * 200) + 500)
    else:
        print("Ingresó una cantidad errónea, vuelva a intentarlo")

llamadas()