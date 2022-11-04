"""
    En cierto pais el descuento que se debe pagar por los articulos
    se calcula mediante la siguiente tabla:

        * Los primeros $20 no causan impuestos
        * los siguientes $20 tienen un 30% de descuento y el resto el 40%

    Si el costo del producto es mayor a $500, se le cobra 50% en ves de 40%
"""
precio = float(input("Ingrese el costo del artículo  "))
precio2 = (precio - 40) * 0.4
precio3 = (precio - 40) * 0.5
veinte = (20 * 0.3)
total = float()
if precio > 500:
    total = precio + precio3 + veinte
elif precio == 20:
    total = precio
else:
    total = precio + precio2 + veinte
print("Precio del artículo después de impuestos $", total)