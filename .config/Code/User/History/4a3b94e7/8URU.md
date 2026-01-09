# ¿Que imprimira en pantalla el siguiente codigo? ¿Cual es el alcance de la variable frase?

```python
frase = "Hola"

def f():
    frase = "Es un lindo dia"
    print(frase)
```

## 1. ¿Que imprimira en pantalla?

La funcion asi como esta no imprimira nada, porque aunque la funcion `f()` esta definida, nunca es **llamada**. Para que imprima algo, tendria que añadirse la linea `f()` al final del codigo.

Si llamas a la funcion (`f()`), el resultado sera:

`Es un lindo dia`

## 2. ¿Cual es el alcance de la variable `frase`?

- **Alcance Global (`frase = "Hola"`):** Esta variable vive en el cuerpo principal del script. Es accesible desde cualquier parte, pero no puede ser modificada dentro de una funcion a menos que se use la palabra clave `global`.

- **Alcance Local (`frase = "Es un lindo dia"`):** Esta variable vive **unicamente dentro** de la funcion `f()`. Se crea cuando la funcion empieza y se destruye cuando termina.

## 3. ¿Que es el "Shadowing"?

Cuando defines una variable local con el mismo nombre que una global, la variable local **"sombra"** o oculta a la global dentro de ese bloque.

- Dentro de la funcion, Python prioriza la variable local.

- Fuera de la funcion, la variable global sigue intacta con el valor
  `"Hola"`.
