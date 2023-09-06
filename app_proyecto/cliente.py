"""
cliente.py:
    Módulo encargado de inicializar un cliente e interactuar con el servidor.
"""
__author__ = "Diego Calderón, Nahuel Vargas"
__maintainer__ = "Diego Calderón, Nahuel Vargas"
__email__ = "diegoacalderon994@gmail.com, nahuvargas24@gmail.com"
__copyright__ = "Copyright 2023"
__version__ = "0.0.1"

import socket
import json


# Creo un socket que utilizará IPs de la familia IPv4 con protocolo TCP.
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Defino IP y puerto al cual me quiero conectar.
host = "localhost"
puerto = 9999

# Intento conectarme al servidor.
try:
    # Me conecto al servidor definido de acuerdo a los parámetros previos.
    clientsocket.connect((host, puerto))

    # Recibo y decodifico mensaje del servidor.
    mensaje = clientsocket.recv(4096)
    print(mensaje.decode("UTF-8"))

    while True:
        mensaje = clientsocket.recv(4096)
        opcion = input(mensaje.decode("UTF-8"))

        if opcion == "1":
            # Codifico y envío opción seleccionada al servidor.
            clientsocket.sendall(opcion.encode("UTF-8"))

            mensaje = clientsocket.recv(4096)

            # json.loads reconstruye la cadena recibida en la lista original.
            lista = json.loads(mensaje.decode("UTF-8"))
            # Imprimo lista de stock total recibida.
            for nom, cant, prec, descrip in lista:
                print(
                    "Nombre: "
                    + nom
                    + ", Cantidad: "
                    + cant
                    + ", Precio: "
                    + prec
                    + ", Descripción: "
                    + descrip
                    + "\n"
                )

        elif opcion == "2":
            # Codifico y envío opción seleccionada al servidor.
            clientsocket.sendall(opcion.encode("UTF-8"))

            mensaje = clientsocket.recv(4096)
            nom = input(mensaje.decode("UTF-8"))

            # Codifico y envío nombre del artículo a consultar.
            clientsocket.sendall(nom.encode("UTF-8"))

            mensaje = clientsocket.recv(4096)
            if mensaje.decode("UTF-8") == "Componente no encontrado":
                print("Componente no encontrado \n")
            else:
                # Si el componente fue encontrado recibio e imprimo sus características.
                lista = json.loads(mensaje.decode("UTF-8"))
                print("Componente encontrado \n")
                for nom, cant, prec, descrip in lista:
                    print(
                        "Nombre: "
                        + nom
                        + ", Cantidad: "
                        + cant
                        + ", Precio: "
                        + prec
                        + ", Descripción: "
                        + descrip
                        + "\n"
                    )

        elif opcion == "3":
            # Codifico y envío opción seleccionada al servidor.
            clientsocket.sendall(opcion.encode("UTF-8"))

            mensaje = clientsocket.recv(1024)
            print(mensaje.decode("UTF-8"))
            break

        else:
            # Codifico y envío opción seleccionada al servidor.
            clientsocket.sendall(opcion.encode("UTF-8"))

            # En este caso recibiré mensaje de opción incorrecta.
            mensaje = clientsocket.recv(1024)
            print(mensaje.decode("UTF-8"))

    # Cierro conexión con el servidor.
    clientsocket.close()

# Si se produce una excepción al intentar conectarme, la capturo y muestro mensaje de error.
except:
    print(
        "La conexión fue rechazada. Compruebe que el servidor esté en funcionamiento."
    )
