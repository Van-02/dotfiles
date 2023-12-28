import datetime
"""
Crear un programa Agenda, que haciendo uso del objeto modelado en el punto anterior, Amigo, 
permita al usuario cargar amigos, la cantidad que desee hasta que presione la "s" de salir.
Estos amigos deberán ser almacenados en una lista enlazada.

Cuando el usuario haya decidido dejar de cargar amigos y presione la tecla de salir, 
se le deberá entonces presentar un menú en pantalla con las siguientes opciones:

1) Mostrar todos los amigos, descartarlos y salir.

2) Almacenarlos en la Agenda, de modo permanente y salir.

En la primera opción, simplemente se mostrarán en pantalla uno a uno, los amigos cargados anteriormente, 
y luego el programa terminará, descartando los datos ingresados.

En la segunda opción, los datos de todos los amigos ingresados, serán guardados 
en un archivo de texto llamado agenda.txt y el programa finalizará.
"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.raiz = None

    def ingresar(self, nuevo_nodo):
        if self.raiz:
            ultimo_nodo = self.raiz

            while ultimo_nodo.siguiente != None:
                ultimo_nodo = ultimo_nodo.siguiente

            ultimo_nodo.siguiente = nuevo_nodo

        else:
            self.raiz = nuevo_nodo

    def mostrar(self):
        aux_nodo = self.raiz

        while aux_nodo != None:
            print(aux_nodo.dato, end=' -> ')
            aux_nodo = aux_nodo.siguiente

        print('Null/Fin')

    def posicion(self, num):
        aux_nodo = self.raiz
        contador = 0

        while aux_nodo != None:
            if contador == num:
                return aux_nodo.dato

            contador += 1
            aux_nodo = aux_nodo.siguiente

        raise Exception('List index out of range')


class Amigo:
    def __init__(self, apellido, apodo, nombre, celular, nacimiento, entorno):
        self.apellido = apellido
        self.apodo = apodo
        self.nombre = nombre
        self.celular = celular
        self.nacimiento = nacimiento
        self.entorno = entorno

    def edad(self):
        hoy = datetime.datetime.today()
        anio = hoy.year
        # La posicion 2 corresponde con el año [dia, mes, año]
        return anio - self.nacimiento[2]


lista = ListaEnlazada()
opcion = None

while opcion != 's':
    lista.ingresar(Nodo(Amigo(
        input('Apellido -> '),
        input('Apodo -> '),
        input('Nombre -> '),
        input('Celular -> '),
        input('Nacimiento -> '),
        input('Entorno -> '))
    ))
    opcion = input("'s' para salir -> ")


while opcion != 's':
    print("1) Mostrar todos los amigos, descartarlos y salir.\n")
    print("2) Almacenarlos en la Agenda, de modo permanente y salir.\n")

    opcion = input()
