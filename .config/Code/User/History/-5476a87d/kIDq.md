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

#### 1. Tipado Estatico vs. Dinamico

- **En C**: Debes declarar el tipo variable antes de usarla (int x = 10;). Esa variable solo podra guardar enteros para siempre.
- **En Python**: El tipo se infiere en tiempo de ejecucion (x = 10). Puedes cambiarlo luego a una cadena (x = "Hola") sin problemas.

#### 2. Precision arbitraria

- **Diferencia clave**: En C, si sumas 1 al maximo valor de un int, ocurre un desbordamiento (overflow) y el numero "da la vuelta" a un valor negativo.
- **En Python**: En Python el int no tiene limite fijo. Si el numero crece, Python simplemente usa mas memoria RAM para guardarlo.

#### 3. Representacion Interna

- **C(Primitivos)**: Un int en C es simplemente una direccion de memoria con 32 bits de datos puros. Es extremadamente rapido.
- **Python(Objetos)**: Un int en Python es un objeto completo. Ademas del valor, guarda informacion sobre su tipo y un contador de referencias para el recolector de basura. Por eso, un "simple" entero en Python ocupa unos 28 bytes, mientras que en C ocupa solo 4.

#### 4. Gestion de Texto

- **C**: No tiene un tipo "String" real. Usa arreglos de caracteres (char[]) que terminan con un caracter nulo (\0). Manejarlos requiere gestionar la memoria manualmente.
- **Python**: Tiene el tipo str, que es una secuencia inmutable de caracteres Unicode muy potente y facil de manipular.
