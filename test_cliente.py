import socket
import codificacion

port = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"Conectando a localhost, puerto {port}.")

client.connect(('localhost', port))

while True:
    msg = input(">> ") #str
    snd = codificacion.codificar(msg)
    if msg == "/exit":
        snd = codificacion.codificar("*El cliente se ha desconectado...*")
        
        client.send(snd.encode())
        break
    print("Enviando...")

    client.send(snd.encode()) #bytes

    print("Mensaje enviado.\nEsperando respuesta...")
    rsp = codificacion.decodificar(client.recv(1024).decode())

    print(f"-- {rsp}")
    if rsp == "*Se ha cerrado el servidor...*":
        break

client.close()