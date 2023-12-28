# Utilizando una pila, invierta una palabra ingresada por el usuario y muestrela en pantalla.

class Pila:
    def __init__(self):
        self.items = []

    def vacio(self):
        return len(self.items) == 0

    def agregar(self, element):
        self.items.append(element)

    def quitar(self):
        if not self.vacio():
            return self.items.pop()
        else:
            raise IndexError("The stack is empty")

    def top(self):
        if not self.vacio():
            return self.items[-1]

        else:
            raise IndexError("The stack is empty")

    def tamanio(self):
        return len(self.items)


def invertir(pila):
    aux_pila = []

    for i in pila.items[]:
        for j in i[:-1]:
            aux_pila.append(j)



palabra = Pila()

palabra.agregar(input("Ingrese una palabra -> "))
invertir(palabra)