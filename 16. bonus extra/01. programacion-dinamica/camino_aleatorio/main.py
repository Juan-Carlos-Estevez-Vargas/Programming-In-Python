from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show


def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_intentos, tipo_borracho):
    borracho = tipo_borracho("Juan")
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_intentos):
        campo = Campo()
        campo.agregar_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias


def graficar(x, y):
    grafica = figure(title="Camino de Borrachos",
                     x_axis_label="pasos", y_axis_label="distancia")
    grafica.line(x, y)
    show(grafica)


def main(distancias_caminata, numero_intentos, tipo_borracho):
    distancias_medias_caminata = []

    for pasos in distancias_caminata:
        distancias = simular_caminata(pasos, numero_intentos, tipo_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_medias_caminata.append(distancia_media)

        print(f"{tipo_borracho.__name__} caminata aleatoria de {pasos} pasos")
        print(f"Media = {distancia_media}")
        print(f"Máxima = {distancia_maxima}")
        print(f"Mínima = {distancia_minima}")

    graficar(distancias_caminata, distancias_medias_caminata)


if __name__ == "__main__":
    distancias_caminata = [10, 100, 1000, 10000]
    numero_intentos = 100

    main(distancias_caminata, numero_intentos, BorrachoTradicional)
