"""
Realizar un programa que lea un numero real e imprima su valor absoluto. El
valor absoluto de un numero x, se escribe |x| y se define como: 
|x| = x cuando x >= 0 
|-x| = x cuando x < 0
"""

number = int(input("Ingrese un numero: "))

print(f"El valor absoluto de {number} es {abs(number)}")
