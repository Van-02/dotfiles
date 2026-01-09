"""
Numero Invertido: Se requiere mostrar en pantalla un numero invertido de 6 
cifras, al que fuera ingresado por teclado. (Ejemplo: en pantalla se vera: 
“El numero ingresado es 140975, invertido es: 579041”)
"""

number = int(input("Enter a 6-digit number: "))
original_number = number
reversed_num = 0

while number > 0:
    # 1. Get the last digit
    last_digit = number % 10

    # 2. Add it to the reversed number (shifting decimals to the left)
    reversed_num = (reversed_num * 10) + last_digit

    # 3. Remove the last digit from the original number
    number = number // 10

print(
    f"The number entered is {original_number}, reversed it is: {reversed_num}")
