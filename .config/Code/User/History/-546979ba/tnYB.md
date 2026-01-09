### Supongamos que nos dan 8 nombres. Queremos seleccionar de alli los nombres que empiecen con la letra M. ¿Como escribiriamos un algoritmo, que realice esa seleccion de nombres? Utilizar español primero para describir la idea de los pasos a seguir, y finalmente escribir un algoritmo en pseudocodigo, con los pasos bien precisos. ¿Encuentra algun problema conceptual que podria tener para implementarlo con los temas aprendidos hasta ahora?

1. Crear una lista con cada nombre.
2. Iterar la lista.
3. Hacer un condicional que verifique que cada nombre que empiece M se imprima en pantalla

```Pseudocodigo
ALGORITMO VerificarNombreM
    VARIABLES:
        names: list
        i: str
    INICIO
        names = ["Ana", "Maria", "Monica", "Martina", "Pedro", "Calvin", "Dario", "Carlos"]

        PARA i EN names HACER:
            SI i[0] == "M" ENTONCES
                MOSTRAR i
    FIN
```
