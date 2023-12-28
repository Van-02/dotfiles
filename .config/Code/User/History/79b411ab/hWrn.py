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


lista = ListaEnlazada()
lista.ingresar(Nodo(1))
lista.ingresar(Nodo(2))
lista.ingresar(Nodo(3))
lista.ingresar(Nodo(4))
lista.mostrar()
print(lista.posicion(3))
