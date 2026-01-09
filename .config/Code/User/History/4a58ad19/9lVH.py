"""
Dado un numero entero formado solo por los digitos 0 (cero) y 1 (uno), diseñe 
una funcion que compruebe si el numero tiene o no la misma cantidad de ceros que 
de unos
"""


def same_amount(number: int) -> bool:
    return str(number).count("0") == str(number).count("1")


# Tests
print(same_amount(1001))
print(same_amount(10))
print(same_amount(110))
print(same_amount(0110))
