"""
    Muchos son los cambios que promueven la pandemia generada por el COVID-19
    y sus variantes; por mencionar algunos: la alimentación, el control del peso,
    etc.  María Fernanda se encuentra preocupada por la salud de su familia, y
    encuentra un artículo para llevar un control sobre el peso, conocido como
    “índice de masa corporal” (IMC) para adultos de 20 años o más.
    El IMC permite establecer una clasificación al relacionar el peso en metros
    con el peso en kilogramos; la relación esta determinada por el
    peso (kg) / estatura (mts) elevada a la 2, que determina un índice y a su vez
    el nivel de peso (bajo peso, normal, sobrepeso y obeso).
"""
peso = float(input("Ingrese su peso en kg por favor  "))
estatura = float(input("Ingrese su estatura en metros  "))
imc = peso / (estatura ** 2)
if imc < 17.5:
    print("Bajo peso")
elif 17.5 <= imc < 24:
    print("Normal")
elif 24 <= imc < 29:
    print("Sobrepeso")
else:
    print("Obeso")