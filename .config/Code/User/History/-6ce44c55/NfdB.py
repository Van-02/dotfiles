# Dada una lista de valores numéricos, determinar la cantidad de números pares de la misma, utilizando recursión.

def pares(lista: list):

    if len(lista) == 0:
        return None

    else:
        es_par = lista[0] % 2 == 0
        valor = lista[0]
        if es_par:
            return valor + pares(lista[1:])

        else:
            return pares(lista[1:])


lista = [0, 1, 2, 3, 4]
print(pares(lista))