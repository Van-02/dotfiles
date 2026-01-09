"""
Crear una funcion llamada delta_de_dirac que tome dos numeros enteros y 
devuelva 1 si ambos numeros son iguales, y 0 sino.
"""


def delta_of_dirac(num_1: int, num_2: int) -> int:
    return int(num_1 == num_2)


num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
result = delta_of_dirac(num_1, num_2)

print(f"Are both numbers equal? {result}")
