def cesar_cipher(text, desplazamiento):

    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resultado = []

    for char in text:
        if char in minusculas:
            indice = (minusculas.index(char) + desplazamiento) % 26
            resultado.append(minusculas[indice])
        
        elif char in mayusculas:
            indice = (mayusculas.index(char) + desplazamiento) % 26
            resultado.append(mayusculas[indice])

        else:
            resultado.append(char)
        
    return ''.join(resultado)

texto_normal = input('Escribe la palabra:')
desplazamiento = int(input('Escriba el numero de desplazamientos en valores enteros:'))
print(cesar_cipher(texto_normal, desplazamiento))