# Dada una lista de valores numéricos, determinar la cantidad de números pares de la misma, utilizando recursión.

def pares(lista):
    if len(lista) == 0:
        return 0

    else:
        return 1 + pares(lista[1:])