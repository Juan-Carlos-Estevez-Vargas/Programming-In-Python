# Realizado por Juan Carlos Estevez Vargas
year = int(input("Ingrese un año por favor  "))
A = year % 19
B = year % 4
C = year % 7
D = (19 * A + 24) % 30
E = (2 * B + 4 * C + 6 * D + 5) % 7
N = (22 + D + E)
if N <= 31:
    print("El domingo de pascua es el ", N, " de Marzo")
else:
    print("El domingo de pascua es el ", N - 31, " de Abril")
