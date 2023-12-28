#!/bin/python3

"""
1. Disenar un algoritmo que a partir de una pila inicial de tres elementos devuelva una pila
invertida de dichos elementos. La pila inicial se encuentra vacia, usted deber ́a apilar los
elementos y mostrar la pila original. Luego invertir los elementos, y mostrar la nueva pila
invertida.
"""

"""
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def mostrar(self):
        print(self.items)


def invertir_pila(pila):
    pila_invertida = Pila()

    while not pila.esta_vacia():
        element = pila.desapilar()
        pila_invertida.apilar(element)

    return pila_invertida


pila = Pila()

pila.apilar(3)
pila.apilar(2)
pila.apilar(1)
pila.mostrar()

pila_invertida = invertir_pila(pila)
pila_invertida.mostrar()

"""

"""
2. Se almacena una palabra en una pila, de a una letra, y se desea imprimir la palabra
invertida.
"""

"""
class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def stack(self, element):
        self.items.append(element)

    def unstack(self):
        if not self.empty():
            return self.items.pop()

    def show(self):
        print(self.items)


def invest_word(stack):
    invest_stack = Stack()

    while not stack.empty():
        element = stack.unstack()
        invest_stack.stack(element)

    string = ''.join(invest_stack.items)
    return string


stack = Stack()

stack.stack('h')
stack.stack('o')
stack.stack('l')
stack.stack('a')

print(invest_word(stack))
"""

"""
3. Lea una palabra e imprima un mensaje indicando si es palindromo o no. Use pilas. Una
palabra es palindromo cuando se lee igual hacia adelante que hacia atras. Ejemplo: oso,
radar, reconocer, rotor, seres, somos, etc.
"""

"""
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

    def show(self):
        print(self.items)

    def to_string(self):
        return "".join(self.items)


def is_palindrome(word):
    stack = Stack()
    for letter in word:
        stack.push(letter)

    reversed_word = ""
    while not stack.empty():
        reversed_word += stack.pop()

    return word == reversed_word


word = "radar"
print(is_palindrome(word))
"""

"""
4. Un conductor maneja de un pueblo origen a un pueblo destino, pasando por varios pueblos.
Una vez en el pueblo destino, el conductor debe regresar a casa por el mismo camino.
Muestre el camino recorrido tanto de ida como de vuelta.
"""

"""
class Path:
    def __init__(self):
        self.place = []

    def empty(self):
        return len(self.place) == 0

    def add(self, element):
        self.place.append(element)

    def pop(self):
        if not self.empty():
            return self.place.pop()

    def show(self):
        print(self.place)


mypath = Path()

mypath.add("Shrine")
mypath.add("Gondor")
mypath.add("Mordor")


def inverse_path(path: object):
    path_alternate = Path()

    while not path.empty():
        element = path.pop()
        path_alternate.add(element)

    return path_alternate


mypath.show()
return_path = inverse_path(mypath)
return_path.show()
"""

"""
5. Lea una cadena y determine si los simbolos ( ) y [ ] estan correctamente balanceados. Si
no lo estan muestre el error indicando el simbolo faltante.
"""

"""
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


class BalanceVerifier:
    def __init__(self, string):
        self.string = string
        self.stack = Stack()
        self.pairs = {')': '(', ']': '['}

    def verify_balance(self):
        for i in self.string:
            if i in '([{':
                self.stack.push(i)

            elif i in ')]}':
                if self.stack.empty() or self.stack.pop() != self.pairs[i]:
                    return f"Error: Unbalanced parentheses or brackets, missing {self.pairs[i]}"

        if self.stack.empty():
            return "The parentheses and brackets are correctly balanced."

            
        else:
            return "Error: Unbalanced parentheses or brackets, there are unclosed elements"


input_string = input("Enter a string with parentheses and brackets: ")
verifier = BalanceVerifier(input_string)
result = verifier.verify_balance()
print(result)
"""

"""
6. Un almacen tiene capacidad para apilar n contenedores. Cada contenedor tiene un numero
de identificacion. Cuando se desea retirar un contenedor especifico, deben retirarse primero
los contenedores que estan encima de el y colocarlos en otra pila, efectuar el retiro y
regresarlos. Codifique los metodos push() y pop() para gestionar los contenedores.
"""


class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def show(self):
        print(self.items)

    def push(self, element):
        self.items.append(element)

    def pop(self):
        container_return = int(input("What container wish delete -> "))
        aux_stack = []
        print(len(self.items) - container_return + 1)

        for i in range(len(self.items)):
            if i == len(self.items) - container_return:
                pass


containers = Stack()
containers.push("Container 1")  # Pos 0
containers.push("Container 2")  # Pos 1
containers.push("Container 3")  # Pos 2
containers.push("Container 4")  # Pos 3
containers.push("Container 5")  # Pos 4
containers.push("Container 6")  # Pos 5
containers.push("Container 7")  # Pos 6
containers.pop()
containers.show()

"""
7. Dado un archivo de texto con algunas lineas de texto dentro, cualesquiera, realizar un
programa que genere un archivo de texto llamado invertido.txt que contenga las lineas en
orden inverso al archivo de texto original.
"""

"""
8. (*)Implementar un Verificador de codigo HTML para chequear que un archivo HTML
sea valido.
Infor: En un documento HTML, el contenido se organiza en etiquetas HTML. Las etiquetas que abren tienen la forma < etiqueta > y las correspondientes etiquetas que cierran
tienen la forma < /etiqueta >
Algunas etiquetas HTML comunes son:
body: el cuerpo del documento
h1: Encabezado
center: Centrado
p: Parrafo
li: elemento de lista
Luego, su verificador debera pedir un archivo de texto con extension correspondiente
.htm o .html y verificar su codigo HTML este correcto. Ejemplo de un archivo .html a
continuacion, puede probar abrirlo con un explorador web para verlo bien.
<body>
<center>
<h1> El Poema del Anillo </h1>
</center>
<p> Tres Anillos para los Reyes Elfos bajo el cielo,
Siete para los Se~nores Enanos en palacios de piedra,
Nueve para los Hombres Mortales condenados a morir,
Uno para el Se~nor Oscuro, sobre el trono oscuro
en la Tierra de Mordor donde se extienden las Sombras.
Un Anillo para gobernarlos a todos. Un Anillo para encontrarlos,
un Anillo para atraerlos a todos y atarlos en las tinieblas
en la Tierra de Mordor donde se extienden las Sombras. </p>
</body>
"""

"""
9. Implementar una calculadora de Notacion Polaca Inversa. Recuerde que la forma en que
usualmente escribimos las expresiones aritmeticas, es usando la notacion de infijo.
"""

"""
10. Implementar una funcion que invierta el orden de las palabras de una frase. Ejemplo: Si
recibe la frase ’Buen dia!’ retornara ’dia! Buen’
"""
