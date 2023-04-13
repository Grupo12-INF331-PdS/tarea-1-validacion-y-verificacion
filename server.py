import socket
import codificacion

port = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', port))

server.listen()

print("Esperando conexiones...")

(client_s, client_a) = server.accept()

print(f"Conectando desde {client_a[0]}:{client_a[1]}.")

while True:
    print("Esperando mensaje de cliente...")
    msg = codificacion.decodificar(client_s.recv(1024).decode())
    print(f"-- {msg}")
    if msg == "*El cliente se ha desconectado...*":
        break
    rsp = input(">> ")
    while len(rsp) > 341:
        print("El límite de caracteres por mensaje es de 342...")
        rsp = input(">> ") #str
    snd = codificacion.codificar(rsp)
    if rsp == "/exit":
        snd = codificacion.codificar("*Se ha cerrado el servidor...*")
        client_s.send(snd.encode())
        break
    client_s.send(snd.encode())
    
client_s.close()

server.close()
