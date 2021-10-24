import socket
from datetime import datetime



HOST = '192.168.100.26'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
dataset = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            now = datetime.now()
            f = open("emotions.txt", 'a')
            data = conn.recv(1024)
            if data:
                conn.sendall(data)
                print('Recieved', repr(data))
                towrite = now.strftime("%m/%d/%Y, %H:%M:%S") + "  " + data.decode() + "\n"
                print(towrite)
                f.write(towrite)
            f.close()
