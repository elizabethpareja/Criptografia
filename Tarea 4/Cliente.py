import socket
import threading
import sys
import random  
import elgamal
import pickle
import sqlite3
import hashlib
import os
from time import *

def enviar():

        h1 = open("hola1-cipher.txt", "r")
        h2 = open("hola2-cipher.txt", "r")
        h3 = open("hola3-cipher.txt", "r")
        h4 = open("hola4-cipher.txt", "r")
        h5 = open("hola5-cipher.txt", "r")
        socket.send(b"olitenipololi")
        print("comenzando envio de archivos")

        for i in h1:
            #print(i)    
            socket.send(i.replace("\n","").encode())
            aHsi = socket.recv(1024).decode()
        socket.send(b"fin")  
        print("El archivo1 ha sido enviado correctamente.")
        h1.close()

        sleep(0.1)
        for i in h2:
            socket.send(i.replace("\n","").encode())
            aHsi = socket.recv(1024).decode()
        socket.send(b"fin")  
        print("El archivo2 ha sido enviado correctamente.")
        h2.close()

        sleep(0.1)
        for i in h3:
            socket.send(i.replace("\n","").encode())
            aHsi = socket.recv(1024).decode()
        socket.send(b"fin")  
        print("El archivo3 ha sido enviado correctamente.")
        h3.close()

        sleep(0.1)
        for i in h4:
            socket.send(i.replace("\n","").encode())
            aHsi = socket.recv(1024).decode()
        socket.send(b"fin") 
        print("El archivo4 ha sido enviado correctamente.")
        h4.close()

        sleep(0.1)
        for i in h5:
            socket.send(i.replace("\n","").encode())
            aHsi = socket.recv(1024).decode()
        socket.send(b"fin")  
        print("El archivo5 ha sido enviado correctamente.")
        h5.close()
        

def hashear():

        print("voy a hashear hermanito, pereme un ratito")

        hola1 = open('hola1.txt','r')
        hola2 = open('hola2.txt','r')
        hola3 = open('hola3.txt','r')
        hola4 = open('hola4.txt','r')
        hola5 = open('hola5.txt','r')

        j1 = open('hola1-hash.txt', 'w')
        j2 = open('hola2-hash.txt', 'w')
        j3 = open('hola3-hash.txt', 'w')
        j4 = open('hola4-hash.txt', 'w')
        j5 = open('hola5-hash.txt', 'w')

        for i in hola1:
    
            m = hashlib.sha3_512(i.encode()).hexdigest()
            #print (m)
            j1.write(m + "\n")

        for i in hola2:
    
            m = hashlib.sha3_512(i.encode()).hexdigest()
            #print (m)
            j2.write(m + "\n")

        for i in hola3:
    
            m = hashlib.sha3_512(i.encode()).hexdigest()
            #print (m)
            j3.write(m + "\n")

        for i in hola4:
    
            m = hashlib.sha3_512(i.encode()).hexdigest()
            #print (m)
            j4.write(m + "\n")
            
        for i in hola5:
    
            m = hashlib.sha3_512(i.encode()).hexdigest()
            #print (m)
            j5.write(m + "\n")
  
    
        hola1.close()
        hola2.close()
        hola3.close()
        hola4.close()
        hola5.close()
        
        j1.close()
        j2.close()
        j3.close()
        j4.close()
        j5.close()

def llamadas():
        
        dix = "cd C:\\Users\\Elizabeth\\Desktop\\Tarea 4  mumi"
        os.system(dix)
        
#+++++++++++++++++++++++++++++++++
        dir1 = "hashcat.exe -m 0 -a 0 -O archivo_1 diccionario_2.dict"
        tiempo_inicio= time()
        os.system(dir1)
        tiempo1 = time()-tiempo_inicio
        print ("tiempo archivo 1:", tiempo1)
        
        dix1 = "hashcat.exe -m 0 -a 0 -O --outfile-format=2 archivo_1 diccionario_2.dict --show >> hola1.txt"
        os.system(dix1)
#+++++++++++++++++++++++++++++++++        
        dir2 = "hashcat.exe -m 10 -a 0 -O archivo_2 diccionario_2.dict"
        tiempo_inicio= time()
        os.system(dir2)
        tiempo2 = time()-tiempo_inicio
        print ("tiempo archivo 2:", tiempo2)

        dix2 = "hashcat.exe -m 10 -a 0 -O --outfile-format=2 archivo_2 diccionario_2.dict --show >> hola2.txt"
        os.system(dix2)
#+++++++++++++++++++++++++++++++++
        dir3 = "hashcat.exe -m 10 -a 0 -O archivo_3 diccionario_2.dict"
        tiempo_inicio= time()
        os.system(dir3)
        tiempo3 = time()-tiempo_inicio
        print ("tiempo archivo 3:", tiempo3)

        dix3 = "hashcat.exe -m 10 -a 0 -O --outfile-format=2 archivo_3 diccionario_2.dict --show >> hola3.txt"
        os.system(dix3)
 #+++++++++++++++++++++++++++++++++
        dir4 = "hashcat.exe -m 1000 -a 0 -O archivo_4 diccionario_2.dict"
        tiempo_inicio= time()
        os.system(dir4)
        tiempo4 = time()-tiempo_inicio
        print ("tiempo archivo 4:", tiempo4)

        dix4 = "hashcat.exe -m 1000 -a 0 -O --outfile-format=2 archivo_4 diccionario_2.dict --show >> hola4.txt"
        os.system(dix4)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        dir5 = "hashcat.exe -m 1800 -a 0 -O archivo_5 diccionario_2.dict"
        tiempo_inicio= time()
        os.system(dir5)
        tiempo5 = time()-tiempo_inicio
        print ("tiempo archivo 5:", tiempo5)

        dix5 = "hashcat.exe -m 1800 -a 0 -O --outfile-format=2 archivo_5 diccionario_2.dict --show >> hola5.txt"
        os.system(dix5)
        

print("Start Cliente")

llamadas()
hashear()

#ACA EMPIEZA
socket = socket.socket()
PORT = 9999

socket.connect(("127.0.0.1",PORT))

socket.send(b"oe enviame la clave publica altoke")
print(">:(")

objetito = socket.recv(1024)
publica = pickle.loads(objetito)

socket.send(b"graciah hermanito")
print(":*")

print ("voy a empezar a encriptar hermanito")

f1 = open('hola1-hash.txt', 'r')
f2 = open('hola2-hash.txt', 'r')
f3 = open('hola3-hash.txt', 'r')
f4 = open('hola4-hash.txt', 'r')
f5 = open('hola5-hash.txt', 'r')

h1 = open('hola1-cipher.txt', 'w')
h2 = open('hola2-cipher.txt', 'w')
h3 = open('hola3-cipher.txt', 'w')
h4 = open('hola4-cipher.txt', 'w')
h5 = open('hola5-cipher.txt', 'w')

for i in f1:
    cipher = elgamal.encrypt(publica, str(i))
    h1.write(cipher + "\n")

for i in f2:
    cipher = elgamal.encrypt(publica, str(i))
    h2.write(cipher + "\n")

for i in f3:
    cipher = elgamal.encrypt(publica, str(i))
    h3.write(cipher + "\n")

for i in f4:
    cipher = elgamal.encrypt(publica, str(i))
    h4.write(cipher + "\n")

for i in f5:
    cipher = elgamal.encrypt(publica, str(i))
    h5.write(cipher + "\n")
    


f1.close()
f2.close()
f3.close()
f4.close()
f5.close()

h1.close()
h2.close()
h3.close()
h4.close()
h5.close()

enviar()

socket.send(b"listo")


print("Ahora espera que el server haga la base de datos, Adios")

socket.close()

