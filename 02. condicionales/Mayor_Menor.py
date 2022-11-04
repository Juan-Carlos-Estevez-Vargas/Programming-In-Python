x = int(input("Ingrese un número  "))
y = int(input("Ingrese un número  "))
z = int(input("Ingrese un número  "))
if x > y and x > z:
    if y > z:
        print("\n", x, "\n", y, "\n", z)
    else:
        print("\n", x, "\n", z, "\n", y)
elif y > x and y > z:
    if x > z:
        print("\n", y, "\n", x, "\n", z)
    else:
        print("\n", y, "\n", z, "\n", x)
elif z > x and z > y:
    if x > y:
        print("\n", z, "\n", x, "\n", y)
    else:
        print("\n", z, "\n", y, "\n", x)
elif x == y and y == z:
    print("\n", z, "\n", y, "\n", x)
