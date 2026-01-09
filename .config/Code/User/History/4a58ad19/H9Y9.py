"""
Dado un numero entero formado solo por los digitos 0 (cero) y 1 (uno), diseñe 
una funcion que compruebe si el numero tiene o no la misma cantidad de ceros que 
de unos
"""


def has_balanced_digits(binary_str: str) -> bool:
    """
    Checks if a binary-like string has the same number of 0s and 1s.

    :param binary_str: A string composed of '0' and '1'.
    :type binary_str: str
    :return: True if counts are equal, False otherwise.
    :rtype: bool
    """
    return binary_str.count("1") == binary_str.count("0")


# Tests
print(has_balanced_digits("1001"))
print(has_balanced_digits("10"))
print(has_balanced_digits("110"))
print(has_balanced_digits("0011"))
