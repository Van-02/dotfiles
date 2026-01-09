"""
Crear un programa que permita al usuario ingresar un numero en base 10 y la base
a la cual desea convertirlo. Mostrar el resultado de la conversion. Siempre que
la base sea menor a 10.
"""


def manual_binary(n: int) -> str:
    """
    Converts a base-10 integer to a binary string.
    """
    if n == 0:
        return "0"

    binary_digits = ""
    while n > 0:
        remainder = n % 2
        binary_digits = str(remainder) + binary_digits
        n = n // 2

    return binary_digits


def manual_octal(n: int) -> str:
    """
    Converts a base-10 integer to a octal string.
    """
    if n == 0:
        return "0"

    octal_digits = ""
    while n > 0:
        remainder = n % 8
        octal_digits = str(remainder) + octal_digits
        n = n // 8

    return octal_digits


number = int(input("Enter a number: "))

while True:
    choise = input("Select base to convert: (2, 8): ")
    if choise in ["2", "8"]:
        break
    print("Invalid option")

if choise == "2":
    print(manual_binary(number))
else:
    print(manual_octal(number))
