"""
Concatenar dos listas en base a sus elementos y posiciones. Es decir, crear dos 
listas del mismo tamaño, y luego armar una tercer lista, a la cual primero se le 
agregue el primer elemento de la lista 1, luego el primer elemento de la 
lista 2. Luego se le agregue el segundo elemento de la lista 1, luego el segundo 
elemento de la lista 2, y asi sucesivamente Ejemplo: Supongamos tenemos una 
lista de frutas y otra de verduras. La tercera quedara:

['Damasco', 'Frutilla', 'Banana']
['zanahoria', 'berenjena', 'tomate']
['damasco', 'zanahoria', 'frutilla', 'berenjena', 'Banana', 'tomate']
"""

list_1 = ['Damasco', 'Frutilla', 'Banana']
list_2 = ['zanahoria', 'berenjena', 'tomate']
list_3 = []

for i in range(len(list_1)):
    list_3.append(i)
    list_3.append(i)

print(list_3)
