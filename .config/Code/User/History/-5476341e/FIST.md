### Determine para cada punto si es correcto o no. Justifique en cada caso

#### 1. n = int("3.41")

Es incorrecto porque la funcion int() no puede truncar la string y convertirla a entero.

#### 2. p = str("hola")

Es correcto, aunque es innecesario usar la funcion str() cuando Python detecta automaticamente que es un dato de tipo str.

#### 3. n = "23" + str(12)

Es correcto, pero no sumaria los numeros sino que sumaria las cadenas de caracteres. El output seria "2312"

#### 4. k = str(10) + str(533)

Es correcto, lo mismo que el punto anterior, se sumarian los caracteres. El output seria "10533".
