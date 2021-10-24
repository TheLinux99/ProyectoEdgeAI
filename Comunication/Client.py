import socket
import time

HOST = '192.168.100.26'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
#prueba
a = "Feliz"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(a.encode())
        data = s.recv(1024)
        print('Received', repr(data))
        time.sleep(2)
