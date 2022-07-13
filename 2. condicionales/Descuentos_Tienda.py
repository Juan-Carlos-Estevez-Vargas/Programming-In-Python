"""
En una tienda efectúan un descuento a los clientes dependiendo del monto de la compra. El descuento
se efectúa en el siguiente criterio:

    * Si el monto es menor que $500 no hay descuento
    * Si el monto está comprendido entre $500 y $1000 -> 5% de descuento
    * Si el monto está comprendido entre $1000 y $7000 -> 11% de descuento
    * Si el monto está comprendido entre $7000 y $15000 -> 18% de descuento
    * Si el monto est mayor a $15000 -> 25% de descuento

    Código realizado por Juan Carlos Estevez Vargas
"""
compra = float(input("Ingrese en valor de la compra  "))
if compra < 500:
    print("No se efectuó ningún desdecuento\nTotal a pagar $", compra)
elif 500 <= compra <= 1000:
    print("Se efectuó un descuento del 5%\nTotal a pagar $", compra - compra * 0.05)
elif 1000 < compra <= 7000:
    print("Se efectuó un descuento del 11%\nTotal a pagar $", compra - compra * 0.11)
elif 7000 < compra <= 15000:
    print("Se efectuó un descuento del 18%\nTotal a pagar $", compra - compra * 0.18)
else:
    print("Se efectuó un descuento del 25%\nTotal a pagar $", compra - compra * 0.25)
