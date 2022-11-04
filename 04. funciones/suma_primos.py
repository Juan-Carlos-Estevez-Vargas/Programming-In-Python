def es_primo(numero):
    n = int(2)
    band = True

    while band and (n < numero):
        if numero % n == 0:
            band = False
        else:
            n += 1

    return band


acumulador = 0

while True:
    numero = int(input("Por favor ingrese un número o 0 / Salir:  "))
    if numero == 0:
        break
    if es_primo(numero):
        acumulador += numero

print("La suma de los números leidos es igual a : ", acumulador)
