import socket
import ssl
import tkinter as tk

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

def conectar_obtener():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        secure_socket = context.wrap_socket(client_socket, server_hostname='ip santiagokali')
        secure_socket.connect(('ip kali', 5555))
        secure_socket.send("clave123".encode())
        respuesta = secure_socket.recv(1024).decode()
        print(respuesta)
        datos_recibidos = secure_socket.recv(1024).decode()
        label_datos.config(text=datos_recibidos)
        
        if "CPU" in datos_recibidos:
            cpu_val = float(datos_recibidos.split("CPU "[1].split("%")[0]))
            if cpu_val > 80.0:
                label_alerta.config(text="Uso de CPU alto", fg="red")
            else:
                label_alerta.config(text="Sistema Estable",fg="green")
    
        secure_socket.close()
    except Exception as e:
        label_datos.config(text="Error de Conexión")
        label_alerta.config(text=str(e), fg="red")
        
ventana = tk.Tk()
ventana.title("Monitoreo - Kali Server")
ventana.geometry("450x250")

label_titulo = tk.Label(ventana, text="Monitor de Procesos Distribuidos", font=("Helvetica", 16, "bold"))
label_titulo.pack(pady=15)

label_datos = tk.Label(ventana, text="Presiona el botón para monitorear...", font=("Helvetica", 14))
label_datos.pack(pady=10)

label_alerta = tk.Label(ventana, text="", font=("Helvetica", 12, "bold"))
label_alerta.pack(pady=5)

btn_actualizar = tk.Button(ventana, text="Obtener Estado del Servidor", command=conectar_obtener, height=2, bg="lightblue")
btn_actualizar.pack(pady=10)

ventana.mainloop()