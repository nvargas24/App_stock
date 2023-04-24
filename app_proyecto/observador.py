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
        if args[0][0] == "agreg":
            print("---"*23)
            print("Se ingresó un nuevo componente con los siguientes parámetros:")
            print(
                "Nombre: "
                + args[0][1]
                + ", Cantidad: "
                + args[0][2]
                + ", Precio: "
                + args[0][3]
                + ", Descripción: "
                + args[0][4]
            )
            print("---"*23)

        elif args[0][0] == "elim":
            print("---"*23)
            print("Se eliminó el siguiente componente: ", args[0][1])
            print("---"*23)

        elif args[0][0] == "modif":
            print("---"*23)
            print("Se actualizó el componente: " + args[0][1] +  ", y se modificaron los siguientes parámetros: ")
            if args[0][2] == 1: # flag_c == 1
                print("Nueva cantidad: ",args[0][3])
            if args[0][4] == 1: # flag_p == 1
                print("Nuevo precio: ",args[0][5])
            if args[0][6] == 1: # flag_d == 1
                print("Nueva descripción: ",args[0][7])
            print("---"*23)
