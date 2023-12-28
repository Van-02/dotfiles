# Utilizando una pila, invierta una palabra ingresada por el usuario y muestrela en pantalla.

class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, element):
        self.items.append(element)

    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            raise IndexError("The stack is empty")

    def top(self):
        if not self.empty():
            return self.items[-1]

        else:
            raise IndexError("The stack is empty")

    def size(self):
        return len(self.items)


palabra = 'hola'

for i in palabra:
    print(i)
