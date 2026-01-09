# Determine cuales variables son locales y cuales son globales en el siguiente fragmento de codigo.

```python
saludo = "Hola


def saludar_mundo():
    mundo = "Mundo!"
    print(saludo, mundo)


def saludar_nombre(nombre):
    print(saludo, nombre)


saludar_mundo()
saludar_nombre("Totoro")
```
