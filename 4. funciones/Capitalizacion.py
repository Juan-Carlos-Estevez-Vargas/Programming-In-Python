"""
    Diseñar un programa que calcule lo siguiente:

    1. Las anualidades de capitalizacion si se conoce el tiempo, el tanto por ciento
       y el capital final a pagar.
    2. El capital c que resta por pagar al cabo de t años conociendo la anualidad
       de capitalizacion y el tanto por ciento.
    3. El número de años que se necesita para pagar un capital c a un tanto por ciento r.
"""
import math


def menu():
    opc = 0
    try:
        while opc != 4:
            print("----------------------------------------\n",
                  "-               CAPITAL                -\n",
                  "----------------------------------------\n",
                  "-  1. Anualidades de capitalización    -\n",
                  "-  2. Capital restante por pagar       -\n",
                  "-  3. Cantidad de años restantes       -\n",
                  "-  4. Salir                            -\n",
                  "----------------------------------------\n")
            opc = int(input("Ingrese su opción  "))

            if opc == 1:
                y = anualidades_capitalizacion()
                print("\nLa capitalización es de : ", y)
            elif opc == 2:
                print("\nEl capital a pagar en t años es de : ", capital_restante(y))
            elif opc == 3:
                print("\nEl tiempo en años que le llevará pagar ese capital es de : ",
                      tiempo_restante(y))
            elif opc == 4:
                break
            else:
                print("\nIngresó una opción incorrecta, vuelva a intentarlo")
                menu()

    except Exception as e:
        print("\n---   Debe ingresar un valor numérico   ---")
        menu()

def anualidades_capitalizacion():
    tiempo = int(input("\nIngrese el tiempo  "))
    porcentaje = int(input("Ingrese el porcentaje  "))
    capital = float(input("Ingrese el capital final a pagar  "))

    aa = (capital * porcentaje) / ((1 + porcentaje) * (math.pow((1 + porcentaje), tiempo) - 1))

    return aa


def capital_restante(x):
    tiempo = int(input("\nIngrese el tiempo que le resta  "))
    porcentaje = int(input("Ingrese el porcentaje  "))
    cc = x * (1 + porcentaje) * ((math.pow((1 + porcentaje), tiempo) - 1) / (porcentaje))

    return cc


def tiempo_restante(x):
    capital = float(input("Ingrese el capital final a pagar  "))
    porcentaje = int(input("Ingrese el porcentaje  "))

    tt = (math.log10(1 + (capital * porcentaje) / (x * (1 + porcentaje)))) / (math.log10(1 + porcentaje))

menu()