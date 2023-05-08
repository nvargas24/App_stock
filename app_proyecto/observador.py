"""
observador.py:
    Módulo encargado de notificar modificaciones a la base de datos y registro de usuarios. 
"""
__author__ = "Diego Calderón, Nahuel Vargas"
__maintainer__ = "Diego Calderón, Nahuel Vargas"
__email__ = "diegoacalderon994@gmail.com, nahuvargas24@gmail.com"
__copyright__ = "Copyright 2023"
__version__ = "0.0.2"

class Sujeto:
    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        self.observadores.remove(obj)

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(args)


class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class ObservadorConcreto(Observador):
    def __init__(self, obj):
        self.observado = obj
        self.observado.agregar(self)

    def update(self, *args):
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

        elif len(args[0]) == 1:
            nombre = args[0]
            print("---" * 23)
            print("Se eliminó el siguiente componente: ", nombre)
            print("---" * 23)

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

        elif args[0][0] == "Consulta":
            ipcl, numcon, fecha, hora = args[0][1:]
            archivo = open("registro_log_serv.txt", "a", encoding="utf-8")
            archivo.write(
                "El cliente con la siguiente ip:"
                + str(ipcl)
                + " y numero de conexión: "
                + str(numcon)
                + ", consultó stock total, "
                + "Fecha: "
                + str(fecha)
                + ", Hora: "
                + str(hora)
                + "\n"
            )

        elif args[0][0] == "Consultacomp":
            nom, ipcl, numcon, fecha, hora = args[0][1:]
            archivo = open("registro_log_serv.txt", "a", encoding="utf-8")
            archivo.write(
                "El cliente con la siguiente ip:"
                + str(ipcl)
                + " y numero de conexión: "
                + str(numcon)
                + ", consultó stock de "
                + nom
                + ", Fecha: "
                + str(fecha)
                + ", Hora: "
                + str(hora)
                + "\n"
            )

        elif args[0][0] == "Cierro":
            ipcl, numcon, fecha, hora = args[0][1:]
            archivo = open("registro_log_serv.txt", "a", encoding="utf-8")
            archivo.write(
                "El cliente con la siguiente ip:"
                + str(ipcl)
                + " y numero de conexión: "
                + str(numcon)
                + ", cerró conexión, "
                + "Fecha: "
                + str(fecha)
                + ", Hora: "
                + str(hora)
                + "\n"
            )
