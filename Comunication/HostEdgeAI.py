import socket
from datetime import datetime



HOST = '192.168.100.63'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
dataset = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        f = open("emotions.txt")
        now = datetime.now()
        while True:
            data = conn.recv(1024)
            #if not data:
                #break
            conn.sendall(data)
            print('Recieved', repr(data))
            f.write(now + "  " + repr(data))
        f.close()
