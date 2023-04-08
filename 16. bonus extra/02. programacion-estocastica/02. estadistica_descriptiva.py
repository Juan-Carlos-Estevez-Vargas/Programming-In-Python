import random
import math


def media(X):
    return sum(X) / len(X)


def varianza(X):
    media_ = media(X)
    acumulador = 0

    for x in X:
        acumulador += (x - media_)**2

    return acumulador / len(X)


def desviacion_estandar(X):
    return math.sqrt(varianza(X))


if __name__ == "__main__":
    X = [random.randint(1, 21) for i in range(20)]
    media_ = media(X)
    varianza_ = varianza(X)
    desviacion_ = desviacion_estandar(X)

    print(X)
    print(media_)
    print(varianza_)
    print(desviacion_)
