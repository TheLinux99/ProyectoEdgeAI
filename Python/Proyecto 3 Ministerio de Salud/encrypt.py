import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
from cryptography.fernet import Fernet
 
#Mensaje original
message = "Ministerio de Salud de Costa Rica. Estado de vacunacion COVID-19: Completo"

#Key para encryptar y desencriptar
key = Fernet.generate_key()

#Se guarda la key para poder desencryptar luego
f = open("cryptokey.txt", "wb")
f.write(key)
f.close()

fernet = Fernet(key)
 
encMessage = fernet.encrypt(message.encode())
 
#encMessage contiene el codigo para poner en el QR

qrcode = pyqrcode.create(encMessage)
qrcode.png('qrvac.png',scale=8)
