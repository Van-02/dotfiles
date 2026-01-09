"""
Crear una funcion que tome un argumento numerico y devuelva ese numero elevado 
al cuadrado. Luego de haber creado la funcion, pedirle al usuario 5 numeros, de 
a uno, e ir mostrando cada numero elevado al cuadrado (utilizando dicha funcion)
"""


def exponentiation(number) -> int:
    return number ** 2


print("Enter 5 numbers")
for i in range(5):
    user_number = int(input(f"Number {i + 1}: "))
    print(f"{user_number}² = {exponentiation(user_number)}")
