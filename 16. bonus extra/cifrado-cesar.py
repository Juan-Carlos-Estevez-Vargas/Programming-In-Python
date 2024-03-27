def cifrar_descrifrar_cesar(mensaje, desplazamiento):
    mensaje = mensaje.lower() # hola, eres maravilloso
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    texto_cifrado = ''

    for letra in mensaje: # o
        if letra in alfabeto:
            indice = alfabeto.find(letra) 
            indice_desplazado = (indice + desplazamiento) % len(alfabeto)
            texto_cifrado += alfabeto[indice_desplazado]
        else:
            texto_cifrado += letra

    return texto_cifrado

mensaje_encriptado = cifrar_descrifrar_cesar('enix, bobp jxoxsfiinpn', 3)

print(f'{mensaje_encriptado}')