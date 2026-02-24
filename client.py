import socket
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_socket = context.wrap_socket(client_socket, server_hostname='ip santiagokali')

secure_socket.connect(('ip kali', 5555))

secure_socket.send("clave123".encode())
respuesta = secure_socket.recv(1024).decode()
print(respuesta)