"""
Crear una funcion llamada es positivo que tome un numero como argumento y 
devuelva verdadero o falso, como valores logicos, si el numero es positivo o no
"""


def is_positive(number: int) -> bool:


"""
    Checks if a number is greater than or equal to zero.
    
    Args:
        number (int): The integer to evaluate.
        
    Returns:
        bool: True if non-negative, False otherwise.
    """
return number >= 0


user_input = int(input("Enter a number: "))
print(is_positive(user_input))
