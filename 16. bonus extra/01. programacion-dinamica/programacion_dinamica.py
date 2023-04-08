import sys


# Implementación de la suscesión de manera recursiva (ineficiente)
def fibonacci_recursivo(n):
    if (n == 0 or n == 1):
        return 1
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)


# Implementación de la suscesión de manera dinámica (eficiente)
def fibonacci_dinamico(n, memoization={}):
    if n == 0 or n == 1:
        return 1

    try:
        return memoization[n]
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, memoization) + fibonacci_dinamico(n - 2, memoization)
        memoization[n] = resultado
        return resultado


if __name__ == "__main__":
    sys.setrecursionlimit(10002)
    n = int(input("Ingrese un número: "))
    #resultado = fibonacci_recursivo(n)
    resultado_dinamico = fibonacci_dinamico(n)
    print(resultado_dinamico)
