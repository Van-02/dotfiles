### ¿Como ordenarias 4 numeros? piensa diferentes estrategias, luego intenta escribir un algoritmo basado en alguna de esas estrategias. Pasalo a pseudocodigo.

Existen varios tipos de algoritmos de ordenamiento como el **Ordenamiento de Burbuja(Bubble Sort), Insercion(Insertion Sort), Rapido(Quick Sort)**

El mas intuitivo es el Ordenamiento de Seleccion (Selection Sort).

### Selection Sort

Vamos a ordenar la lista: [29, 10, 14, 37, 13]

    Paso 1: Buscamos el menor en toda la lista. Es el 10. Lo intercambiamos con el primero (29).

        Resultado: [10, 29, 14, 37, 13]

    Paso 2: Buscamos el menor desde la posición 2 en adelante. Es el 13. Lo intercambiamos con el segundo (29).

        Resultado: [10, 13, 14, 37, 29]

    Paso 3: Buscamos el menor desde la posición 3. Es el 14. Ya está en su lugar, no hay intercambio.

        Resultado: [10, 13, 14, 37, 29]

    Paso 4: Buscamos el menor entre 37 y 29. Es el 29. Lo intercambiamos con el 37.

        Resultado: [10, 13, 14, 29, 37]

¡Listo! La lista está ordenada.

```Pseudocodigo
ALGORITMO OrdenamientoPorSeleccion
    VARIABLES:
        lista[] <- [29, 10, 14, 37, 13]
        entero: n <- longitud(lista)
        entero: i, j, indice_minimo, temporal

    INICIO
        PARA i DESDE 0 HASTA n - 2 HACER
            indice_minimo <- i  // Suponemos que el primero es el menor

            // Buscar el menor en el resto de la lista
            PARA j DESDE i + 1 HASTA n - 1 HACER
                SI lista[j] < lista[indice_minimo] ENTONCES
                    indice_minimo <- j
                FIN_SI
            FIN_PARA

            // Intercambiar el mínimo encontrado con el elemento i
            temporal <- lista[indice_minimo]
            lista[indice_minimo] <- lista[i]
            lista[i] <- temporal
        FIN_PARA
    FIN
```

Recursos:

[Algoritmos de Ordenamiento por Chio Code](https://www.youtube.com/playlist?list=PLfBtpqIBIz7qyXl8TK8KPHYylRVlvIFY8)
