"""
    Realice un programa que permita calcular el promedio de notas de un curso
"""
estudiantes = int(input("Ingrese la cantidad de alumnos  "))
promedio = 0
for i in range(estudiantes):
    nota = float(input("Ingrese la nota final del alumno N°" + str(i + 1) + " : "))
    promedio += nota
print("\nEl promedio general del salón de clase es : ", (promedio / estudiantes))
