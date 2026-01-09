"""
Dado un n ingresado por el usuario, realizar la suma de los n primeros 
terminos de la serie a continuacion. Mostrar el resultado.

1/1 + 1/2 + 1/3 + 1/4 + ... 1/n
"""

number = int(input("Please enter a number: "))
result = 0

for i in range(1, number + 1):
    print(i)
