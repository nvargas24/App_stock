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
            print("---"*23)
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
            print("---"*23)

        elif len(args[0]) == 1:
            nombre = args[0]
            print("---"*23)
            print("Se eliminó el siguiente componente: ", nombre)
            print("---"*23)

        elif len(args[0]) == 7:
            nombre, flag_c, cantidad, flag_p, precio, flag_d, descrip = args[0]
            print("---"*23)
            print("Se actualizó el componente: " + nombre +  ", y se modificaron los siguientes parámetros: ")
            if flag_c == 1:
                print("Nueva cantidad: ", cantidad)
            if flag_p == 1: 
                print("Nuevo precio: ", precio)
            if flag_d == 1:
                print("Nueva descripción: ", descrip)
            print("---"*23)
