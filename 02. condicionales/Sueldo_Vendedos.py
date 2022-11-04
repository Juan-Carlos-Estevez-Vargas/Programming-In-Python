"""
Determine el sueldo mensual normal y neto de un Vendedor, tomando en cuenta
que este tiene un sueldo base más una comisión por sus ventas realizadas en el mes.
Y del sueldo total anterior, se le descuentan la retención (10%) y el EPS (3.07%).
El porcentaje de comisión mensual de la venta mensual se indica en la siguiente tabla:
"""
salario_base = float(input("Ingrese el salario base del trabajador  "))
ventas = float(input("Ingrese las ventas realizadas por el trabajador  "))

if ventas < 60.5:
    ventas *= 0.05
elif 60.5 <= ventas < 80:
    ventas *= 0.1
elif 80 <= ventas < 200:
    ventas *= 0.18
elif ventas >= 200:
    ventas *= 0.25

retencion = (salario_base + ventas) * 0.1
eps = (salario_base + ventas) * 0.0307

print("Salario base : ", salario_base,
      "\nComisión : ", ventas,
      "\nDescuento Retención : ", retencion,
      "\nDescuento EPS : ", eps,
      "\nSalario Neto : ", salario_base + ventas - retencion - eps)
