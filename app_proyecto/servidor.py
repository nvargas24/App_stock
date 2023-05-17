"""
servidor.py:
    Módulo encargado de iniciar servidor y atender las conexiones entrantes. 
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
    Clase que contiene métodos para inicializar el servidor y manejar las conexiones entrantes.
    """

    def __init__(self, obj):
        """
        Constructor que llama a método que enciende el servidor

        param obj: objeto de clase ``Crud()`` que se crea en la ventana ``MainWindow()``
        """
        self.obj_c = obj
        self.lanza_servidor()

    def lanza_servidor(self):
        """
        Metodo que se encarga de inicializar el host y port del servidor, establecer conexión
        e interactuar con el cliente.
        """

        # Creo un socket que utilizará IPs de la familia IPv4 con protocolo TCP.
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host = "localhost"  # Esta es la IP del servidor.
        puerto = 9999  # Puerto en el cual estoy escuchado.
        print("Iniciando servidor desde: ", host)

        # Asocio el socket con el host y puerto indicado.
        serversocket.bind((host, puerto))

        # Pongo al servidor en modo de escucha, con una cola de hasta 3 conexiones entrantes.
        serversocket.listen(3)

        while True:
            # Acepto una conexión entrante.
            # Recibo socket por el cual el cliente se conectó y los datos sobre su conexión.
            clientsocket, address = serversocket.accept()
            ipcl, numcon = address
            print(
                "Recibo la conexión desde IP: "
                + str(ipcl)
                + ", con número de conexión: "
                + str(numcon)
            )

            # Codifico y envío mensaje al cliente.
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

                # Recibo y decodifico opción enviada por el cliente.
                mjedec = clientsocket.recv(1024).decode("UTF-8")

                # Si seleccionó la primera opción envío una lista con el stock total de componentes.
                if mjedec == "1":
                    data_from_db = self.obj_c.leer_db(None)
                    for row in data_from_db:
                        registro = (
                            row.nombre,
                            row.cantidad,
                            row.precio,
                            row.descripcion,
                        )
                        self.lista.append(registro)

                    # json.dumps convierte la lista a una cadena como si fuese un string.
                    # Envío la información solicitada por el socket empleado por el cliente.
                    clientsocket.send(json.dumps(self.lista).encode("UTF-8"))

                    # Notifico a observador.
                    self.obj_c.notificar(
                        "Consulta",
                        ipcl,
                        numcon,
                        datetime.datetime.today().strftime("%d/%m/%y"),
                        datetime.datetime.today().strftime("%H:%M:%S"),
                    )

                # Si seleccionó la segunda opción envío los datos del componente solicitado.
                elif mjedec == "2":
                    mensaje = "Ingrese el nombre del componente: "
                    clientsocket.send(mensaje.encode("UTF-8"))
                    mjerec = clientsocket.recv(1024)
                    nom = mjerec.decode("UTF-8")

                    if self.obj_c.leer_db(nom):
                        data_from_db = self.obj_c.leer_db(nom)
                        for row in data_from_db:
                            registro = (
                                row.nombre,
                                row.cantidad,
                                row.precio,
                                row.descripcion,
                            )
                            self.lista.append(registro)

                        # json.dumps convierte la lista a una cadena como si fuese un string.
                        # Envío la información solicitada por el socket empleado por el cliente.
                        clientsocket.send(json.dumps(self.lista).encode("UTF-8"))
                    else:
                        # Si no se encontró el componente solicitado se informará al cliente.
                        mensaje = "Componente no encontrado"
                        clientsocket.send(mensaje.encode("UTF-8"))

                    # Notifico a observador.
                    self.obj_c.notificar(
                        "Consultacomp",
                        nom,
                        ipcl,
                        numcon,
                        datetime.datetime.today().strftime("%d/%m/%y"),
                        datetime.datetime.today().strftime("%H:%M:%S"),
                    )

                # Si seleccionó la tercera opción se cierra conexión con el cliente.
                elif mjedec == "3":
                    mensaje = "Conexión terminada"
                    clientsocket.send(mensaje.encode("UTF-8"))

                    # Notifico a observador.
                    self.obj_c.notificar(
                        "Cierro",
                        ipcl,
                        numcon,
                        datetime.datetime.today().strftime("%d/%m/%y"),
                        datetime.datetime.today().strftime("%H:%M:%S"),
                    )
                    break

                # Si seleccionó otra opción distinta a las indicadas, se enviará mensaje de error.
                else:
                    mensaje = "Opción incorrecta, intente nuevamente.\n"
                    clientsocket.send(mensaje.encode("UTF-8"))

                    # Notifico a observador.
                    self.obj_c.notificar(
                        "Error",
                        ipcl,
                        numcon,
                        datetime.datetime.today().strftime("%d/%m/%y"),
                        datetime.datetime.today().strftime("%H:%M:%S"),
                    )

            # Cierro conexión con el cliente.
            clientsocket.close()
            print(
                "Cierro la conexión con IP: "
                + str(ipcl)
                + ", y número de conexión: "
                + str(numcon)
            )
