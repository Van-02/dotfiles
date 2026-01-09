# En el siguiente fragmento de codigo, ¿Que considera es un error o una practica a evitar? Justifique.

```python
def funcion_algo(a, b):
    a = 45
    return(2 \* a) - b
```

El error seria redefinir la variable adentro de la funcion, puesto que el usuario ya le esta pasando el valor de a. Por lo tanto estariamos modificando el valor del usuario.
