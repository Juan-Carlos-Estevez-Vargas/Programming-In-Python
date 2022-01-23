# Juan Carlos Estevez Vargas
num = int(input("Ingrese un numero por favor : "))

millar = (int(num / 1000)) * 1000
centenas = (int((num - millar) / 100)) * 100
decenas = (int((num - millar - centenas) / 10)) * 10
unidades = (int((num - millar - centenas - decenas)))

romano = str()

if (millar == 2000):
    romano += "MM"
else:
    romano += "M"

if (centenas == 100):
    romano += "C"
elif (centenas == 200):
    romano += "CC"
elif (centenas == 300):
    romano += "CCC"
elif (centenas == 400):
    romano += "CD"
elif (centenas == 500):
    romano += "D"
elif (centenas == 600):
    romano += "DC"
elif (centenas == 700):
    romano += "DCC"
elif (centenas == 800):
    romano += "DCCC"
elif (centenas == 900):
    romano += "CM"

if (decenas == 10):
    romano += "X"
elif (decenas == 20):
    romano += "XX"
elif (decenas == 30):
    romano += "XXX"
elif (decenas == 40):
    romano += "XL"
elif (decenas == 50):
    romano += "L"
elif (decenas == 60):
    romano += "LX"
elif (decenas == 70):
    romano += "LXX"
elif (decenas == 80):
    romano += "LXXX"
elif (decenas == 90):
    romano += "XC"

if (unidades == 1):
    romano += "I"
elif (unidades == 2):
    romano += "II"
elif (unidades == 3):
    romano += "III"
elif (unidades == 4):
    romano += "IV"
elif (unidades == 5):
    romano += "V"
elif (unidades == 6):
    romano += "VI"
elif (unidades == 7):
    romano += "VII"
elif (unidades == 8):
    romano += "VIII"
elif (unidades == 9):
    romano += "IX"

print(romano)
