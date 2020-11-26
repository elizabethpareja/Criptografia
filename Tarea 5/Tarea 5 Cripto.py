import imaplib
import configparser
import os
import pprint
import re

##Archivo de texto con correo y contraseña
k=0
hola2 = open('Correo y contraseña.txt','r')
for v in hola2:
    k=k+1
    if (k==1):
        correo2 = v
    if (k==2):
        passw = v
correo2 = correo2.strip()
passw = passw.strip()

imap_host = 'imap.gmail.com'
imap_user = correo2
imap_pass = passw

# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host)

## login to server
imap.login(imap_user, imap_pass)
imap.select('Inbox')

##Archivo de texto
k=0
hola1 = open('Expresion regular.txt','r')
for v in hola1:
    k=k+1
    if (k==1):
        fecha = v
    if (k==2):
        correo = v
    if (k==3):
        regular = v

correo = correo.strip()
fecha = fecha.strip()
regular = regular.strip()
print(fecha, correo, regular)

if regular=='[0-9a-f]{32}@mailing\.redsalud\.cl':
    print("si es igual el regular")
else:
    print(regular + 'no es igual ha [0-9a-f]{32}@mailing\.redsalud\.cl')

##buscar correo
resultado, data = imap.search(None, 'FROM', correo, '(SINCE ' + fecha + ')')

##msg ID
i=0
for num in data[0].split():
    i = i+1
    typ, data1 = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
    j=data1[0][1].decode()
    j = j.replace("<", "")
    j = j.replace(">", "")
    j = j.replace("Message-ID:", "")
    j = j.replace("Message-Id:", "")
    j = j.strip()
    print(str(i) + ". Message-ID: " + j)

    ##Comparar message Id con expresion regular.
    
    r1 = re.fullmatch(regular, j) 
    if r1!=None:    
        print(str(i) + ". match :)" + "\n")
    else:
        print(str(i) + ". NO match, Alerta de correo falso!!! :(" + "\n")       
 
imap.close()


