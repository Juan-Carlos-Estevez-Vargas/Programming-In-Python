#Conversión metros a pulgadas Juan Carlos Estevez Vargas
def menu():
    print("\n¿Qué tipo de conversión desea?\n"
          "1. Metros a Pulgadas\n"
          "2. Pulgadas a Metros\n")
    num = int(input("Ingrese su opción -> "))
    if num == 1:
        metros = float(input("Ingrese el número de metros -> "))
        print("La cantidad de pulgadas son: ", metros*39.37)
        menu()
    elif num == 2:
        pulgadas = float(input("Ingrese el número de pulgadas -> "))
        print("El número de metros es: ", pulgadas*0.0254)
        menu()
    else:
        print("Opcion incorrecta")
        menu()
menu()