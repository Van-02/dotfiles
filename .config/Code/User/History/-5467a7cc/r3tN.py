"""
Intenta implementar un programa que utilice una de las estrategias anteriores
para ordenar cuatro numeros de menor a mayor, ingresados por el usuario.
"""


def selection_sort(list):
    n = len(list)
    for i in range(n):
        # Encontrar el mínimo en lo que queda de lista
        min_idx = i
        for j in range(i + 1, n):
            if list[j] < list[min_idx]:
                min_idx = j

        # Intercambiar (solo una vez por cada posición i)
        list[i], list[min_idx] = list[min_idx], list[i]


numbers = []

for i in range(4):
    number = int(input("Ingrese un numero: "))
    numbers.append(number)

selection_sort(numbers)
print(f"Lista ordenada: {numbers}")
