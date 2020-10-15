import blowfish
import binascii
import base64
from os import urandom

var = True
while var:
    print( "ingrese su mensaje de 8 caracteres")
    mensaje = input()
    p = len(mensaje)
    if p==8:
       var=False
var = True
while var:
    print("ingrese una llave de 5 caracteres")
    llave = input()
    p = len(llave)
    if p==5:
       var=False
var = True
while var:
    print("ingrese una iv de 8 caracteres")
    ive = input()
    p = len(ive)
    if p==8:
       var=False
llave2 = llave.encode()

cipher = blowfish.Cipher(llave2)
data = mensaje.encode() #data to encrypt, multiplo de 8
iv = ive.encode() # initialization vector, tiene que ser 8
#iv = urandom(8)

data_encrypted = b"".join(cipher.encrypt_cbc(data, iv))

data_encrypted_b64 = base64.b64encode(data_encrypted)#b64
data_decrypted_b64 = base64.b64decode(data_encrypted_b64)#b64 decode

data_encryptedb_hex = binascii.hexlify(data_encrypted) #hexadecimal

data_decrypted = b"".join(cipher.decrypt_cbc(data_encrypted, iv))#desencriptar

data_decrypted2 = data_decrypted.decode() #mensaje original sin "b"
cipher_b64 = data_encrypted_b64.decode() #b64 sin "b"

print(cipher_b64)
print("llave")
print(data_encrypted)
print(data_decrypted_b64)
print(str(data_encrypted, "ascii", "replace"))

a="""<p>Este sitio contiene un mensaje secreto</p>
    <div class="Blowfish" id="""+cipher_b64+"""></div>
    <div class="key" id="""+llave+"""></div>
    <div class="iv" id="""+ive+"""></div>"""

with open(r"a.html", 'w') as f:
    f.write(a)
    
