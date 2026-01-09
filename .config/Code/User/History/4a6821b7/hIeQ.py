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
    target_base = int(input("Select base to convert: (2, 9): "))

    if 2 <= target_base < 10:
        break
    print("Invalid base. Please choose a base between 2 and 9.")

result = convert_base(number, target_base)
print(f"The number {number} in base {target_base} is: {result}")
