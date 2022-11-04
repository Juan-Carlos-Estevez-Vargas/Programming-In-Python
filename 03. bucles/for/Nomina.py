"""
    Crear un programa que permita calcular la nómina para x trabajadores
"""
nomina = 0
for i in range(10):
    sueldo = float(input("Ingrese el sueldo del trabajador N°" + str(i + 1) +" : "))
    nomina += sueldo
print("\nValor total de nómina : ", nomina)