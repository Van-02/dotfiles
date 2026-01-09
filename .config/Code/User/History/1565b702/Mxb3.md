# Describa lo que significa que un argumento sea pasado por valor versus pasado por referencia.

## 1. Pasado por valor (Pass by Value)

cuando pasas un argumento **por valor**, el programa crea una **copia** de la variable original y se la entrega a la funcion.

- **¿Que sucede dentro?**: La funcion trabaja con la copia. Cualquier cambio que realices dentro de la funcion no afecta a la variable original fuera de ella.
- **Contexto tipico:** Se suele dar en tipos de datos simples o primitivos

## 2. Pasado por referencia (Pass by Reference)

Cuando pasas un argumento por referencia, no se crea una copia. En su lugar, se pasa la dirección de memoria (el puntero) de la variable original.

- **¿Qué sucede dentro?** La función tiene acceso directo al espacio de memoria de la variable original. Si modificas el valor dentro de la función, la variable original **también cambia.**

- **Contexto típico:** Se usa para objetos complejos (listas, diccionarios, clases) o para ahorrar memoria al no duplicar datos grandes.
