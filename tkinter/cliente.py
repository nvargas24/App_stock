import socket
import json

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
puerto = 9999
clientsocket.connect((host, puerto))
mensaje = clientsocket.recv(4096)
print(mensaje.decode("UTF-8"))
while True:
    mensaje = clientsocket.recv(4096)
    opcion = input(mensaje.decode("UTF-8"))
    if opcion == "1":
        clientsocket.sendall(opcion.encode("UTF-8"))
        mensaje = clientsocket.recv(4096)
        # json.loads reconstruye la cadena en la lista original
        lista = json.loads(mensaje.decode("UTF-8"))
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
        clientsocket.sendall(opcion.encode("UTF-8"))
        mensaje = clientsocket.recv(4096)
        nom = input(mensaje.decode("UTF-8"))
        clientsocket.sendall(nom.encode("UTF-8"))
        mensaje = clientsocket.recv(4096)
        if mensaje.decode("UTF-8") == "Componente no encontrado":
            print("Componente no encontrado \n")
        else:
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

    else:
        clientsocket.sendall(opcion.encode("UTF-8"))
        mensaje = clientsocket.recv(1024)
        print(mensaje.decode("UTF-8"))
        break

clientsocket.close()
