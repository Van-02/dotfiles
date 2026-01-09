"""
Escriba una funcion que calcule la enesima potencia de un numero, recibiendo 
como parametro un numero real base y otro entero llamado exponente.
La definicion de la funcion es: y = x**n donde x representa la base y n representa 
el exponente.
Nota: tener en cuenta que n puede ser un numero negativo.
Ejemplo: 2 ** 3 = 8 y 2 ** -3 = 0.125
"""


def power(number: int, exponent: int):
    return number ** exponent


print(power(2, 3))
print(power(2, -3))
