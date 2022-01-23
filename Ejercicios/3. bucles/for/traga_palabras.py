"""
    Tu tarea aquí es aún más especial que antes: ¡Debes rediseñar el devorador de vocales
    (feo) del laboratorio anterior (3.1.2.10) y crear un mejor devorador de vocales (bonito)
    mejorado! Escribe un programa que use:

        * Un ciclo for.
        * El concepto de ejecución condicional (if-elif-else).
        * La declaración continue.
    
    Tu programa debe:

        * Pedir al usuario que ingrese una palabra.
        * Utilizar userWord = userWord.upper() para convertir la palabra ingresada por el 
          usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper()
          muy pronto, no te preocupes.
        * Usar la ejecución condicional y la instrucción continue para "comer" las siguientes
          vocales A, E, I, O, U de la palabra ingresada.
        * Asigne las letras no consumidas a la variable palabrasinVocal e imprime la variable 
          en la pantalla.   
    
    Analiza el código en el editor. Hemos creado palabrasinVocal y le hemos asignado una
    cadena vacía. Utiliza la operación de concatenación para pedirle a Python que combine
    las letras seleccionadas en una cadena más larga durante los siguientes giros de ciclo,
    y asignarlo a la variable palabrasinVocal.
"""
userWord = input('Ingresa una palabra por favor  ').upper()
vocales = ('A', 'E', 'I', 'O', 'U')

for letra in vocales:
    userWord = userWord.replace(letra, '')

print(userWord)

