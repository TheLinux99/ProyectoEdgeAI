import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
from cryptography.fernet import Fernet
 
#Mensajes originales
message1 = "Ministerio de Salud de Costa Rica. Estado de vacunacion COVID-19: Completo"
message2 = "Ministerio de Salud de Costa Rica. Estado de vacunacion COVID-19: Incompleto"

#Key para encriptar y desencriptar
#key = Fernet.generate_key()

#Se carga la key para poder encriptar el mensaje
f = open("cryptokey.txt", "rb")
key = f.read()
f.close()

fernet = Fernet(key)
 
encMessage1 = fernet.encrypt(message1.encode())
encMessage2 = fernet.encrypt(message2.encode())
 
#encMessage contiene el codigo para poner en el QR

qrcode1 = pyqrcode.create(encMessage1)
qrcode1.png('qrvac1.png',scale=8)

qrcode2 = pyqrcode.create(encMessage2)
qrcode2.png('qrvac2.png',scale=8)
