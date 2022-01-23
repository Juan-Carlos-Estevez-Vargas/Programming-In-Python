"""
    De una empresa de N empleados, necesitamos obtener el número de empleado y
    sueldo del trabajador con el mayor sueldo de la empresa
"""
mayor = 0
numero_empleado = 0

num_empleados = int(input("Ingrese el número de empleados pertenecientes a la empresa   "))

for i in range(num_empleados):
    sueldo = float(input("Ingrese el salario del trabajador N°" + str(i + 1) + " $"))
    if sueldo > mayor:
        mayor = sueldo
        numero_empleado = i + 1

print("\nEl empleado N°", numero_empleado, " cuenta con el salario mas alto de la empresa",
      "\nSalario : $", mayor)