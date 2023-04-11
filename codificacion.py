def codificar(mensaje):
    mensaje_codificado = ""
    for letra in mensaje:
        # Convertir cada letra en su correspondiente valor ASCII en formato de 3 dígitos
        ascii_code = str(ord(letra)).zfill(3)
        mensaje_codificado += ascii_code
    
    return mensaje_codificado


def decodificar(mensaje_codificado):
    mensaje_decodificado = ""
    i = 0
    while i < len(mensaje_codificado):
        # Leer cada grupo de 3 dígitos y convertirlo en su correspondiente letra ASCII
        ascii_code = int(mensaje_codificado[i:i+3])
        letra = chr(ascii_code)
        mensaje_decodificado += letra
        i += 3
    
    return mensaje_decodificado
