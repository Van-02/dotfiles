"""
Crear un programa que permita al usuario ingresar un numero en base 10 y la base
a la cual desea convertirlo. Mostrar el resultado de la conversion. Siempre que
la base sea menor a 10.
"""


def convert_base(n: int, base: int) -> str:
    """
    Converts a base-10 integer to any base between 2 and 9.
    """
    if n == 0:
        return "0"

    digits = ""
    while n > 0:
        remainder = n % base
        digits = str(remainder) + digits
        n = n // 2

    return digits


number = int(input("Enter a decimal number: "))

while True:
    choise = input("Select base to convert: (2, 8): ")
    if choise in ["2", "8"]:
        break
    print("Invalid option")

if choise == "2":
    print(manual_binary(number))
else:
    print(manual_octal(number))
