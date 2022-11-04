"""
    Como seguramente sabrás, debido a algunas razones astronómicas, el año puede ser bisiesto
    o común. Los primeros tienen una duración de 366 días, mientras que los últimos tienen 
    una duración de 365 días.

    Desde la introducción del calendario gregoriano en 1582, se utiliza la siguiente regla 
    para determinar el tipo de año.

        * Si el número del año NO es divisible entre 4, es un año común
        * De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto
        * De lo contrario, si el número del año no es divisible entre 400, es un año común
        * De lo contrario, es un año bisiesto
"""


def anio_bisiesto():
    try:
        anio = int(input('Ingresa un año por favor  '))

        if anio > 1582:
            if (anio % 4 and anio % 400 != 0):
                print(f'El año {anio} es común')
            else:
                print(f'El año {anio} es bisiesto')
        else:
            print('El año ingresado NO está dentro del periodo del calendario gregoriano')
            anio_bisiesto()
    except Exception:
        print('Ingresaste datos erroneos, vuelve a intentarlo')
        anio_bisiesto()


anio_bisiesto()
