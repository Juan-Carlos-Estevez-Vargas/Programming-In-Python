"""
    ¿Sabes lo que es Mississippi? Bueno, es el nombre de uno de los estados y rios en los 
    Estados Unidos. El rio Mississippi tiene aproximadamente 2340 millas de largo, lo que 
    lo convierte en el segundo rio mas largo de los Estados Unidos(el mas largo es el rio
    Missouri). ¡Es tan largo que una sola gota necesita 90 dias para recorrer toda su
    longitud.

    La palabra Mississippi también se usa para un propósito ligeramente diferente: para 
    contar mississippily.

    Si no estás familiarizado con la frase, estamos aquí para explicarte lo que significa:
    se utiliza para contar segundos.

    La idea detrás de esto es que agregar la palabra Mississippi a un número al contar los
    segundos en vo alta hace que suene mas cercano al reloj, y por tanto "un Mississippi, dos
    Mississippi, tres mississippi" tomará aproximadamente unos tres segundos reales de 
    tiempo. A menudo lo usan los niños que juegan al escondite para asegurarse de que el
    buscador haga un conteo honesto.

    Tu tarea es muy simple aquí, escribe un programa que use un ciclo for para "contar de 
    forma mississippi" hasta cinco. Habiendo contado hasta cinco, el programa debería 
    imprimir en la pantalla el mensaje final "¡Listo o no, ahí voy!"
"""
import time

for i in range(1, 6):
    print(f'{i} Mississippi')
    time.sleep(1)
print('¡Listo o no, ahí voy!')


