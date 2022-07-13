def es_primo(numero):
    n = int(2)
    band = True

    while band and (n < numero):
        if numero % n == 0:
            band = False
        else:
            n += 1

    return band


acumulador = 0 # Suma todos los números primos.
cantPrimos = 0 # Nos muestra la cantidad de primos ingresados.
cantTotal = 0 # Nos muestra la cantidad de números totales ingresados.

while True:
    numero = int(input('Favor ingresar un número mayor que 2 y menor que 1000 o 0 para salir.  '))

    if (numero == 0):
        break
    if (numero < 2 or numero > 1000):
        print('No es un número válido, por favor ingresa otro  ')
    elif (es_primo(numero)):
        acumulador += numero
        cantPrimos += 1
    
    cantTotal += 1

print(f'\nLa suma de los números primos es: {acumulador} ')
print(f'La cantidad de números primos es: {cantPrimos} ')
print(f'La cantidad de los números ingresados es: {cantTotal}\n ')
