"""
Realizar un programa que lea un numero real e imprima su valor absoluto. El
valor absoluto de un numero x, se escribe |x| y se define como: 
|x| = x cuando x >= 0 
|-x| = x cuando x < 0
"""

number = int(input("Ingrese un numero: "))

if number >= 0:
    print(f"El valor absoluto de {number} es {number}")
elif number < 0:
    print(f"El valor absoluto de {number} es {number * -1}")

# En python existe la funcion abs() que devuelve el valor absoluto de un numero
