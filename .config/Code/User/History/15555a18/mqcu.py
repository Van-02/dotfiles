"""
Crear una funcion llamada es positivo que tome un numero como argumento y 
devuelva verdadero o falso, como valores logicos, si el numero es positivo o no
"""


def is_positive(number: int) -> bool:
    if number >= 0:
        return True
    else:
        return False


user_input = int(input("Enter a number: "))
print(is_positive(user_input))
