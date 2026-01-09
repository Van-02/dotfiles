"""
Numero Invertido: Se requiere mostrar en pantalla un numero invertido de 6 
cifras, al que fuera ingresado por teclado. (Ejemplo: en pantalla se vera: 
“El numero ingresado es 140975, invertido es: 579041”)
"""

number = input("Enter a number: ")
inverted_number = number[::-1]

print(f"Number ingresed: {number}")
print(f"Number inverted: {inverted_number}")
