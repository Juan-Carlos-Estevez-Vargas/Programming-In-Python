"""
Pida al usuario la edad y el sexo, para que la computadora le indique si ya puede
jubilarse. Tome en cuenta que un hombre se puede jubilar cuando
tenga 60 años o más, en cambio, una mujer mayor se jubilará si tiene más de 54 años.
"""
edad = int(input("Ingrese su edad por favor  "))
sexo = input("Ingrese su sexo (masculino/femenino)  ")

if (edad >= 60 and sexo == "masculino") or (edad >= 54 and sexo.__eq__("femenino")):
    print("Puede jubilarse")
else:
    print("Aún no puede jubilarse")