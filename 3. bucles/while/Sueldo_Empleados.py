nomina = 0
sueldoTrabajador = 0
contador = 0
while contador < 8:
    sueldo = float(input("\nIngrese el sueldo del trabajador N°" + str(contador + 1) + " : "))
    if sueldo < 1000:
        sueldo *= 1.15
        nomina += sueldo
        print("El nuevo sueldo del trabajador es : ", (sueldo))
    else:
        sueldo *= 1.12
        nomina += sueldo
        print("El nuevo sueldo del trabajador es : ", (sueldo))
    contador += 1

print("\nTotal nómina : ", nomina)