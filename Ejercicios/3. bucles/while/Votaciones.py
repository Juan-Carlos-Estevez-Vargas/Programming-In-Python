"""
    Genere un algoritmo que permita simular una votación: posteriormente,
    muestre que candidato ganó y cuantos votos obtuvo.
"""
votantes = int(input("Ingrese la cantidad de votantes  "))
candidato1 = 0
candidato2 = 0
candidato3 = 0
blanco = 0
nulo = 0
print("\n-------------------------------\n"
      "          VOTACIONES          -\n"
      "-------------------------------\n"
      "- 1.    Candidato 1           -\n"
      "- 2.    Candidato 2           -\n"
      "- 3.    Candidato 3           -\n"
      "- 4.    Voto en blanco        -\n"
      "-------------------------------\n")
for i in range(votantes):
    voto = int(input("Ingrese su voto  "))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 4:
        blanco += 1
    else:
        nulo += 1

if candidato1 > candidato2 and candidato1 > candidato3 and candidato1 > blanco and candidato1 > nulo:
    print("\nEl candidato 1 es el ganador con ", candidato1, " votos")
elif candidato2 > candidato3 and candidato2 > blanco and candidato2 > nulo and candidato2 > candidato1:
    print("\nEl candidato 2 es el ganador con ", candidato2, " votos")
elif candidato3 > blanco and candidato3 > nulo and candidato3 > candidato1 and candidato3 > candidato2:
    print("\nEl candidato 3 es el ganador con ", candidato3, " votos")
elif blanco > candidato3 and blanco > nulo and blanco > candidato1 and blanco > candidato2:
    print("\nGanó el voto en blanco con ", blanco, " votos")
else:
    print("\nDemasiados votos nulos con ", nulo, " votos")
