import socket


#host = '127.0.0.1'
port = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"Conectando a localhost, puerto {port}.")

client.connect(('localhost', port))

flag = True
while flag:
    msg = input(">> ") #str
    print("Enviando...")
    client.send(msg.encode()) #bytes
    
    rsp = client.recv(1024)
    print(f"-- {rsp.decode()}")

    cont = input("Continuar?: ")
    if cont == "N":
        flag = False

client.close()