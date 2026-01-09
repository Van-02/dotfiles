# Determine cuales variables son locales y cuales son globales en el siguiente fragmento de codigo.

```python
saludo = "Hola"


def saludar_mundo():
    mundo = "Mundo!"
    print(saludo, mundo)


def saludar_nombre(nombre):
    print(saludo, nombre)


saludar_mundo()
saludar_nombre("Totoro")
```

## 1. Variables Globales

Solo hay una variable global:

- `saludo`: Definida en el cuerpo principal del script. Es accesible por ambas funciones (`saludar_mundo` y `saludar_nombre`) porque el ambito global engloba a todo el programa.

## 2. Variables Locales

Hay dos variables locales:

- `mundo`: Es una variable local de la funcion `saludar_mundo()`. Solo existe dentro de esa funcion.

- `nombre`: Aunque es un **parametro**, los parametros se comportan como variables locales. Solo existe dentro de `saludar_nombre()` y toma el valor que le pases al llamarla (en este caso, `"Totoro"`).
