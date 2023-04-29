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
    def __init__(self, obj_crud, obj_db):
        self.observado = obj_crud
        self.data_base = obj_db
        self.observado.agregar(self)

    def update(self, *args):
        # Agregar nuevo articulo
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

            if self.data_base.leer_db(nombre):
                return "Ya existe articulo"
            else:
                self.data_base.agregar_db(nombre, cantidad, precio, descrip)
                return "Nuevo articulo cargado"

        # Eliminar articulo
        elif len(args[0]) == 1:
            nombre = args[0]

            if self.data_base.leer_db(nombre):
                print("---"*23)
                print("Se eliminó el siguiente componente: ", nombre)
                print("---"*23)
                self.data_base.eliminar_db(nombre)
                return "Articulo eliminado"
            else:
                return "Articulo no encontrado"

        # Modificar articulo
        elif len(args[0]) == 7:
            nombre, flag_cant, cantidad, flag_precio, precio, flag_descrip, descrip = args[0]
            print("---"*23)
            print("Se actualizó el componente: %s y se modificaron los siguientes parámetros: " %nombre)
            self.data_base.actualizar_db(nombre, cantidad, precio, descrip)

            if flag_cant == 1: # flag_c == 1
                print("Nueva cantidad: ", cantidad)
            if flag_precio == 1: # flag_p == 1
                print("Nuevo precio: ", precio)
            if flag_descrip == 1: # flag_d == 1
                print("Nueva descripción: ", descrip)
            print("---"*23)

            return "Se modifico articulo"



