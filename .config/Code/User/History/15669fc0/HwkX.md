# En el siguiente fragmento de codigo, ¿Que considera como una practica a evitar? Justifique y reescriba su version del codigo si considera que hay una forma mas correcta de definir la funcion suma.

```python
def sumar(a, b):
    print(a + b)
```

Encuentro dos errores en el codigo:

1. No hay retorno de la funcion
2. Hace un print del calculo. Si bien no es un problema en si, hace el codigo
   inservible para su reutilizacion futura.

La forma correcta seria:

```Python
def sumar(a, b):
    return (a + b)
```
