"""
Crear una funcion que tome un argumento numerico y devuelva ese numero elevado 
al cuadrado. Luego de haber creado la funcion, pedirle al usuario 5 numeros, de 
a uno, e ir mostrando cada numero elevado al cuadrado (utilizando dicha funcion)
"""


def square(number: int) -> int:
    # Returns the square of a given integer
    return number ** 2


print("Enter 5 numbers to see their squares: ")

for i in range(5):
    user_input = int(input(f"Enter number {i + 1}: "))
    result = square(user_input)
    print(f"{user_input}² = {result}")
