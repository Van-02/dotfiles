# Dada una lista de valores numéricos, determinar la cantidad de números pares de la misma, utilizando recursión.

def pares(lista):
    if len(lista) == 0:
        return 0

    else:
        if lista[0] % 2 == 0:
            return 1 + pares(lista[1:])

        else:
            return pares(lista[1:])


lista = [0, 1, 2, 3, 4, 5, 6]
print(f"Hay {pares(lista)} numeros pares")
