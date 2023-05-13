"""
observador.py:
    Módulo encargado de notificar modificaciones a la base de datos, y acciones de usuarios que se conecten al servidor. 
"""
__author__ = "Diego Calderón, Nahuel Vargas"
__maintainer__ = "Diego Calderón, Nahuel Vargas"
__email__ = "diegoacalderon994@gmail.com, nahuvargas24@gmail.com"
__copyright__ = "Copyright 2023"
__version__ = "0.0.1"


class Sujeto:
    """
    Clase que contiene métodos para el manejo de observadores.
    """

    # Lista que almacena los observadores creados.
    observadores = []

    def agregar(self, obj):
        """
        Método que agrega un observador creado a la lista **observadores**.

        :param obj: Objeto de clase ``ObservadorConcreto()``.
        """
        self.observadores.append(obj)

    def quitar(self, obj):
        """
        Método que elimina un observador de la lista **observadores**.

        :param obj: Objeto de clase ``ObservadorConcreto()``.
        """
        self.observadores.remove(obj)

    def notificar(self, *args):
        """
        Método que notifica, a todos los observadores creados, de una acción asociada al objeto que siguen.

        :param args: Parámetros que reciben del objeto que observan.
        """

        for observador in self.observadores:
            observador.update(args)


class Observador:
    """
    Clase que genera una excepción si se intenta notificar a un objeto de la misma.
    Esto se debe a que esta clase delega la tarea de seguimiento a los objetos de sus clases hijas.
    """

    def update(self):
        """
        Método que genera una excepción si se intenta notificar a una instancia de la clase ``Observador()``.
        """
        raise NotImplementedError("Delegación de actualización")


class ObservadorConcreto(Observador):
    """
    Clase que inicializa al observador y define su accionar en función de la notificación recibida.
    """

    def __init__(self, obj):
        """
        Constructor que define el objeto a seguir y agrega el observador creado a la lista **observadores**.

        :param obj: Objeto a observar.
        """
        self.observado = obj
        self.observado.agregar(self)

    def update(self, *args):
        """
        Método que notifica al observador de una acción asociada al objeto que sigue y en función de ello realiza algo.

        :param args: Parámetros que recibe del objeto que observa.
        """
        # Si se ingresó un nuevo artículo lo informará por consola.
        if len(args[0]) == 4:
            nombre, cantidad, precio, descrip = args[0]
            print("---" * 23)
            print("Se ingresó un nuevo componente con los siguientes parámetros:")
            print(
                "Nombre: "
                + nombre
                + ", Cantidad: "
                + cantidad
                + ", Precio: "
                + precio
                + ", Descripción: "
                + descrip
            )
            print("---" * 23)

        # Si se eliminó un artículo lo informará por consola.
        elif len(args[0]) == 1:
            nombre = args[0][0]
            print("---" * 23)
            print("Se eliminó el siguiente componente: ", nombre)
            print("---" * 23)

        # Si se modificó un artículo lo informará por consola
        # indicando que parámetros fueron modificados.
        elif len(args[0]) == 7:
            nombre, flag_c, cantidad, flag_p, precio, flag_d, descrip = args[0]
            print("---" * 23)
            print(
                "Se actualizó el componente: "
                + nombre
                + ", y se modificaron los siguientes parámetros: "
            )
            if flag_c == 1:
                print("Nueva cantidad: ", cantidad)
            if flag_p == 1:
                print("Nuevo precio: ", precio)
            if flag_d == 1:
                print("Nueva descripción: ", descrip)
            print("---" * 23)

        # Si el cliente, conectado al servidor, consulta el stock total de componentes
        # escribe en un archivo de log dicha acción junto con la información de conexión del cliente.
        elif args[0][0] == "Consulta":
            ipcl, numcon, fecha, hora = args[0][1:]
            archivo = open("registro_log_serv.txt", "a", encoding="utf-8")
            archivo.write(
                "El cliente con la siguiente ip:"
                + str(ipcl)
                + " y número de conexión: "
                + str(numcon)
                + ", consultó stock total, "
                + "Fecha: "
                + str(fecha)
                + ", Hora: "
                + str(hora)
                + "\n"
            )

        # Si el cliente, conectado al servidor, consulta el stock de un componente
        # escribe en un archivo de log dicha acción junto con la información de conexión del cliente.
        elif args[0][0] == "Consultacomp":
            nom, ipcl, numcon, fecha, hora = args[0][1:]
            archivo = open("registro_log_serv.txt", "a", encoding="utf-8")
            archivo.write(
                "El cliente con la siguiente ip:"
                + str(ipcl)
                + " y número de conexión: "
                + str(numcon)
                + ", consultó stock de "
                + nom
                + ", Fecha: "
                + str(fecha)
                + ", Hora: "
                + str(hora)
                + "\n"
            )

        # Si el cliente, conectado al servidor, finaliza la conexión
        # escribe en un archivo de log dicha acción junto con la información de conexión del cliente.
        elif args[0][0] == "Cierro":
            ipcl, numcon, fecha, hora = args[0][1:]
            archivo = open("registro_log_serv.txt", "a", encoding="utf-8")
            archivo.write(
                "El cliente con la siguiente ip:"
                + str(ipcl)
                + " y número de conexión: "
                + str(numcon)
                + ", cerró conexión, "
                + "Fecha: "
                + str(fecha)
                + ", Hora: "
                + str(hora)
                + "\n"
            )
