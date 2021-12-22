"""
Dada las siguientes notas almacenadas en un arreglo:
[20, 15, 12, 11, 8, 4, 1]
Elimine la nota más baja programáticamente sin usar la función (min) y escriba en pantalla. 
Luego programáticamente calcule el promedio de notas descontando la nota eliminada.
"""
# Arreglo original
A = [20, 15, 12, 11, 8, 4, 1]

#Asignar el mínimo
maxi = 20
mini = maxi 

# Recorrer el arreglo para conseguir el minimo del array
for i in A:
    if i < mini:
        mini = i

# Imprimiendo el mínimo
print(f'El minimo del array es: {mini}')

# Removiendo mini del array
A.remove(mini)

suma = 0
for j in A:
    suma += j

print(f'Promedio sin la nota mas baja {suma / len(A)}')