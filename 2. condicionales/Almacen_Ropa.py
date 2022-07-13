"""
Un almacén de venta de ropa tiene las siguientes promociones para sus clientes,
las cuales consisten en lo siguiente
(pago en efectivo = E, pago con Tarjeta de Crédito = T):

    a. Para ventas menores ó iguales a 100.000, con pago en efectivo,
        se hace un descuento del 20% y si es con tarjeta de crédito, se hace el 10%.
    b. Para ventas mayores a 100.000 y menores o iguales a 200.0000, con pago
        en efectivo, se hace un descuento del 30%, con tarjeta de crédito se hace el 15%.
    c. Para ventas mayores a 200.000, con pago en efectivo, se hace un descuento del 40% y
        con tarjeta de crédito se hace el 20%. Indique el valor del descuento y el
        total a pagar.
"""
def pago():
    pago = int(input("\n------------------------------------------------------------\n"
                     "-     ¿Con qué medio de pago desea realizar su compra?     -\n"
                     "------------------------------------------------------------\n"
                     "-     1. En efectivo                                       -\n"
                     "-     2. Tarjeta de Crédito                                -\n"
                     "------------------------------------------------------------\n"))
    if pago == 1:
        promocion(1)
    elif pago == 2:
        promocion(2)
    else:
        print("Opción incorrecta")
        pago()


def promocion(n):
    compra = float(input("Ingrese el valor de su compra  "))
    if 0 <= compra <= 1000 and n == 1:
        compra -= (compra * 0.2)
        print("El descuento es: ", (compra * 0.2))
        print("Valor total a pagar : ", compra)
    elif 0 <= compra <= 1000 and n == 2:
        compra -= (compra * 0.1)
        print("El descuento es: ", (compra * 0.1))
        print("Valor total a pagar : ", compra)
    elif 1000 < compra <= 2000 and n == 1:
        compra -= (compra * 0.3)
        print("El descuento es: ", (compra * 0.3))
        print("Valor total a pagar : ", compra)
    elif 1000 < compra <= 2000 and n == 2:
        compra -= (compra * 0.15)
        print("El descuento es: ", (compra * 0.15))
        print("Valor total a pagar : ", compra)
    elif compra > 2000 and n == 1:
        compra -= (compra * 0.4)
        print("El descuento es: ", (compra * 0.4))
        print("Valor total a pagar : ", compra)
    elif compra > 2000 and n == 2:
        compra -= (compra * 0.2)
        print("El descuento es: ", (compra * 0.2))
        print("Valor total a pagar : ", compra)
    else:
        print("Ingresó un valor incorrecto, vuelva a intentarlo")

pago()