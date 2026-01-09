# ¿Que imprimira en pantalla el siguiente codigo? Determine el alcance de cada variable.

```Python
x = 3

def f():
    y = x + 1
    print(x)


    def g():
        x = 1
        print(y)
        print(x)


    g()


f()
```

| Variable | Ubicacion       | Alcance respecto a `g()`                               |
| -------- | --------------- | ------------------------------------------------------ |
| `x = 3`  | Global          | **Global**(Ignorada en `g` porque tiene su propia `x`) |
| `y = 4`  | Dentro de `f()` | **Enclosing**(Accesible para lectura en `g`)           |
| `x = 1`  | Dentro de `g()` | **Local** (Solo existe dentro de `g`)                  |
