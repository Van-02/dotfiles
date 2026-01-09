## Determine si este fragmento de codigo da error, y en caso afirmativo, explique porque.

```python
def imprimir_nro():
    n = 1
    print("El primer numero es: ", n)


imprimir_nro()
print("El primer numero es: ", n)
```

Si, este codigo dara un error. Especificamente, lanzara un `NameError`.

### ¿Por que da error?

El problema radica en el **Scope**(alcance) de la variable.

1. La variable `n` esta definida dentro de la funcion `imprimir_nro()`. Esto la convierte en una variable local.

2. Las variables locales solo existen mientras la funcion se esta ejecutando y solo son visibles dentro de ella.

3. Cuando intentas ejecutar el ultimo `print("El primer numero es: ", n)` Python busca la variable `n` en el ambito global (fuera de la funcion) y no la encuentra, porque `n` "murio" en cuanto la funcion termino su ejecucion.
