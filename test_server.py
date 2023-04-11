import socket


#host = '127.0.0.1'
port = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', port))

server.listen()

print("Esperando conexiones...")

(client_s, client_a) = server.accept()

print(f"Conectando desde {client_a[0]}:{client_a[1]}.")



flag = True
while flag:
    msg = client_s.recv(1024)
    print(f"-- {msg.decode()}")

    rsp = input(">> ")

    client_s.send(rsp.encode())

    cont = input("Continuar?: ")
    if cont == "N":
        flag = False

client_s.close()

server.close()