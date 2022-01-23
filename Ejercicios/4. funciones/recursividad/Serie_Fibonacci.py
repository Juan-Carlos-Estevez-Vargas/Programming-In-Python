numero = int(input("Ingrese un número  "))


def fibonacci(numero):
    if numero < 2:
        return numero
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)

for i in range(numero):
    print(fibonacci(i))
