def codificar(mensaje):
    # Reemplazar cada letra por su correspondiente ASCII
    mensaje_codificado = ""
    for letra in mensaje:
        mensaje_codificado += str(ord(letra))
    
    return mensaje_codificado


def decodificar(mensaje_codificado):
    # Convertir cada conjunto de 3 dígitos en su correspondiente letra ASCII
    mensaje_decodificado = ""
    for i in range(0, len(mensaje_codificado), 3):
        letra_ascii = int(mensaje_codificado[i:i+3])
        mensaje_decodificado += chr(letra_ascii)
    
    return mensaje_decodificado
