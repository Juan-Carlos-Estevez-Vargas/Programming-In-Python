# Codigo realizado por Juan Carlos Estevez Vargas
horas = int(input("Ingrese el número de horas trabajadas  "))
years = int(input("Ingrese la cantidad de años que lleva en la empresa  "))
impuesto = float()
salario2 = float()
salario = float()
bonificacion = float()
if horas <= 38:
    salario = horas * 15000
else:
    h = horas - 38
    salario2 = h * (15000 + 15000 * 0.5)
    salario = horas * 15000 + salario2

if salario > 570000:
    impuesto = salario * 0.1
else:
    impuesto = salario * 0.05

if years >= 10:
    bonificacion = salario + 200000
else:
    bonificacion = salario

print("Salario bruto : ", salario,
      "\nImpuesto : ", impuesto,
      "\nSalario neto : ", bonificacion - impuesto)