"""
servidor.py:
    Módulo encargado de iniciar servidor. 
"""
__author__ = "Diego Calderón, Nahuel Vargas"
__maintainer__ = "Diego Calderón, Nahuel Vargas"
__email__ = "diegoacalderon994@gmail.com, nahuvargas24@gmail.com"
__copyright__ = "Copyright 2023"
__version__ = "0.0.1"

import socket
import json
import datetime

class Serv:
    """
    Clase que contiene metodos para inicializar el servidor
    """
    def __init__(self, obj):
        """
        Constructor que llama a metodo que lanza al servidor
        param obj: objeto Crud que se crea en la ventana MainWindow
        """
        self.obj_c = obj
        self.lanza_servidor()

    def lanza_servidor(self):
        """
        Metodo que se encarga de inicializar el host y port del servidor, establecer conexion
        e interactuar con el cliente
        """
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "localhost"  # Esta es la IP del servidor
        puerto = 9999  # Puerto en el cual estoy escuchado
        print("Iniciando servidor desde: ", host)
        serversocket.bind((host, puerto))
        serversocket.listen(3)

        while True:
            # Inicia la conexión
            clientsocket, address = serversocket.accept()
            ipcl, numcon = address
            print(
                "Recibo la conexión desde IP: "
                + str(ipcl)
                + ", con número de conexión: "
                + str(numcon)
            )

            mensaje = "Hola, Bienvenido al servidor de Electronica del oeste"
            clientsocket.send(mensaje.encode("UTF-8"))

            while True:
                self.lista = []
                mensaje = (
                    "Elija una opción: "
                    + "\n"
                    + "1 Para ver Catálogo completo "
                    + "\n"
                    + "2 Para Consultar stock de un componente"
                    + "\n"
                    + "3 Para cerrar conexión"
                    + "\n"
                    + "Opción: "
                )
                clientsocket.send(mensaje.encode("UTF-8"))
                mjerec = clientsocket.recv(1024)
                if mjerec.decode("UTF-8") == "1":
                    data_from_db = self.obj_c.leer_db(None)
                    for row in data_from_db:
                        mensaje = (
                            row.nombre,
                            row.cantidad,
                            row.precio,
                            row.descripcion,
                        )
                        self.lista.append(mensaje)
                    # json.dumps convierte la lista a una cadena como si fuese un string
                    clientsocket.send(json.dumps(self.lista).encode("UTF-8"))
                    # Notifico a observador
                    self.obj_c.notificar(
                        "Consulta",
                        ipcl,
                        numcon,
                        datetime.datetime.today().strftime("%d/%m/%y"),
                        datetime.datetime.today().strftime("%H:%M:%S"),
                    )

                elif mjerec.decode("UTF-8") == "2":
                    mensaje = "Ingrese el nombre del componente: "
                    clientsocket.send(mensaje.encode("UTF-8"))
                    mjerec = clientsocket.recv(1024)
                    nom = mjerec.decode("UTF-8")

                    if self.obj_c.leer_db(nom):
                        data_from_db = self.obj_c.leer_db(nom)
                        for row in data_from_db:
                            mensaje = (
                                row.nombre,
                                row.cantidad,
                                row.precio,
                                row.descripcion,
                            )
                            self.lista.append(mensaje)
                        # json.dumps convierte la lista a una cadena como si fuese un string
                        clientsocket.send(json.dumps(self.lista).encode("UTF-8"))
                    else:
                        mensaje = "Componente no encontrado"
                        clientsocket.send(mensaje.encode("UTF-8"))

                    # Notifico a observador
                    self.obj_c.notificar(
                        "Consultacomp",
                        nom,
                        ipcl,
                        numcon,
                        datetime.datetime.today().strftime("%d/%m/%y"),
                        datetime.datetime.today().strftime("%H:%M:%S"),
                    )

                elif mjerec.decode("UTF-8") == "3":
                    mensaje = "Conexión terminada"
                    clientsocket.send(mensaje.encode("UTF-8"))

                    # Notifico a observador
                    self.obj_c.notificar(
                        "Cierro",
                        ipcl,
                        numcon,
                        datetime.datetime.today().strftime("%d/%m/%y"),
                        datetime.datetime.today().strftime("%H:%M:%S"),
                    )
                    break

            clientsocket.close()
