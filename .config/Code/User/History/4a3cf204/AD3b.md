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
