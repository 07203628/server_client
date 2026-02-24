import socket
import ssl
import psutil

host = 0
port = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

print ("Servidor seguro escuchando...")
while True:
    client_socket, addr = server_socket.accept()
    secure_socket = context.wrap_socket(client_socket, server_side=True)
    
    token = server_socket.recv(1024).decode()
    if token == "clave123":
        secure_socket.send("Autenticado. Iniciando monitoreo...".encode())
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        datos = f"CPU: {cpu}% | RAM: {ram}"
        secure_socket.send(datos.encode())
        
    else:
        secure_socket.send("Acceso denegado.".encode())
        secure_socket.close()