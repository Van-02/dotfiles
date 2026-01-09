### Investigue en Internet sobre los tipos de datos de C, y la especificacion de cada uno. Compare con los de Python.

En el mundo de la programación, C y Python representan filosofías opuestas: C es un lenguaje de "bajo nivel" (cerca del hardware) y Python es de "alto nivel" (cerca del lenguaje humano). Esta diferencia se refleja profundamente en sus tipos de datos.

### Especificacion de los Tipos de Datos en C

En C, los tipos de datos tienen un tamaño fijo en memoria (que puede variar segun la arquitectura del procesador, usualmente 32 o 64 bits). Se definen en la cabecera <limits.h>

| Tipo      | Tamaño Comun      | Rango Aproximado                          |
| --------- | ----------------- | ----------------------------------------- |
| char      | 1 byte (8 bits)   | -128 a 127                                |
| int       | 4 bytes (32 bits) | -2,147,483,648 a 2,147,483,647            |
| short     | 2 bytes (16 bits) | -32,768 a 32,767                          |
| long long | 8 bytes (64 bits) | ± 9 x 10^18                               |
| float     | 4 bytes           | Precisión simple (6-7 dígitos decimales)  |
| double    | 8 bytes           | Precisión doble (15-17 dígitos decimales) |

### Comparacion: C vs. Python

#### 1. Tipado
