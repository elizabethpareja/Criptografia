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

#por favor esperar a que el servidor imprima "hola" antes de correr el cliente

x = elgamal.generate_keys()
publica = x["publicKey"]
privado = x["privateKey"]
objetito = pickle.dumps(publica)
print("hola")

#------------------------------------------------------------------------------

PORT = 9999
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1',PORT))
server.listen(1000)

def basedatos():
        
        conn = sqlite3.connect('BaseDeDatos.db')
        c = conn.cursor()
        g1 = open('hola1-hash-actualzado.txt', 'r')
        g2 = open('hola2-hash-actualzado.txt', 'r')
        g3 = open('hola3-hash-actualzado.txt', 'r')
        g4 = open('hola4-hash-actualzado.txt', 'r')
        g5 = open('hola5-hash-actualzado.txt', 'r')
        
        c.execute('''CREATE TABLE tabla
                     (numero INTEGER PRIMARY KEY AUTOINCREMENT, archivo1, archivo2, archivo3, archivo4, archivo5)''')

        for i in g1:
            c.execute("INSERT INTO tabla(archivo1) VALUES (?) ;", (i,))

        for i in g2:
            c.execute("INSERT INTO tabla(archivo2) VALUES (?) ;", (i,))
    
        for i in g3:
            c.execute("INSERT INTO tabla(archivo3) VALUES (?) ;", (i,))
    
        for i in g4:
            c.execute("INSERT INTO tabla(archivo4) VALUES (?) ;", (i,))
            
        for i in g5:
            c.execute("INSERT INTO tabla(archivo5) VALUES (?) ;", (i,))

        conn.commit()
        g1.close()
        g2.close()
        g3.close()
        g4.close()
        g5.close()
        conn.close()
        print("se creo la base de datos")


def recibir(sock, addr):


        print("Start Server")

        mensaje = sock.recv(1024).decode()
        print(mensaje)
        
        sock.send(objetito)
        
        mensaje2 = sock.recv(1024).decode()
        print(mensaje2)
#+------------------------------------------------------------------
        aHsi = sock.recv(1024).decode()
        g1 = open('hola1-hash-actualzado.txt', 'w')
        print("voy a empezar a recibir los archivos hermanito")
        print("toy recibiendo el 1 oe")
        while True:
            input_data = sock.recv(4096).decode('utf-8-sig')
            input_data = input_data.replace("\n", "")
            if input_data == "fin":
                    break
            cipher = elgamal.decrypt(privado, input_data)
            g1.write(cipher)
            sock.send(b"olitenipololi")
        print("El archivo 1 se ha recibido correctamente.")
        g1.close()
#+------------------------------------------------------------------
        g2 = open('hola2-hash-actualzado.txt', 'w')
        print("toy recibiendo el 2 oe")
        while True:
                
                input_data = sock.recv(4096).decode('utf-8-sig')
                input_data = input_data.replace("\n", "")
                if input_data == "fin":
                        break
                cipher = elgamal.decrypt(privado, input_data)
                #print(cipher)
                g2.write(cipher)
                sock.send(b"olitenipololi")
        print("El archivo 2 se ha recibido correctamente.")
        g2.close()
#+------------------------------------------------------------------
        g3 = open('hola3-hash-actualzado.txt', 'w')
        print("toy recibiendo el 3 oe")
        while True:
                
            input_data = sock.recv(4096).decode('utf-8-sig')
            input_data = input_data.replace("\n", "")
            if input_data == "fin":
                    break
            cipher = elgamal.decrypt(privado, input_data)
            g3.write(cipher)
            sock.send(b"olitenipololi")
        print("El archivo 3 se ha recibido correctamente.")
        g3.close()
#+------------------------------------------------------------------
        g4 = open('hola4-hash-actualzado.txt', 'w')
        print("toy recibiendo el 4 oe")
        while True:
                
            input_data = sock.recv(4096).decode('utf-8-sig')
            input_data = input_data.replace("\n", "")
            if input_data == "fin":
                    break
            cipher = elgamal.decrypt(privado, input_data)
            g4.write(cipher)
            sock.send(b"olitenipololi")
        print("El archivo 4 se ha recibido correctamente.")
        g4.close()
#+------------------------------------------------------------------
        g5 = open('hola5-hash-actualzado.txt', 'w')
        print("toy recibiendo el 5 oe")
        while True:
                
            input_data = sock.recv(4096).decode('utf-8-sig')
            input_data = input_data.replace("\n", "")
            if input_data == "fin":
                    break
            cipher = elgamal.decrypt(privado, input_data)
            g5.write(cipher)
            sock.send(b"olitenipololi")
        print("El archivo 4 se ha recibido correctamente.")
        g5.close()
#+------------------------------------------------------------------

        msg = sock.recv(1024).decode()      
        print(msg)    
        basedatos()
        sock.close()
        
while True:
	sock, addr = server.accept()
	tarea = threading.Thread(target = recibir, args = (sock, addr))
	tarea.start()



	


