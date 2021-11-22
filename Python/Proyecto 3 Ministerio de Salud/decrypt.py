import os
from cryptography.fernet import Fernet

#Lee el QR y lo transforma en el formato correcto
rawcode = os.popen("python barcode.py -i qrvac.png")
stringcode = rawcode.read()
encMessage = bytes(stringcode, "UTF-8")

#Lee la key con la que se encrypto
f = open("cryptokey.txt", "rb")
key = f.read()
f.close()

fernet = Fernet(key)

#Se desencrypta el codigo QR
decMessage = fernet.decrypt(encMessage).decode()
 
print(decMessage)
