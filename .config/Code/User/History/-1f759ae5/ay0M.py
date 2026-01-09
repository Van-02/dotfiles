"""
Permitir ingresar al usuario un numero de un digito. Controlando se haya 
ingresado dicho numero de no mas de 1 digito de longitud, pasarlo a letras y 
mostrarlo en pantalla. (Ejemplo: Si ingresa 3, se vera como resultado ”tres”).
"""

number = int(input("Ingrese un numero: "))

if number < 0 or number > 9:
    print("Numero incorrecto")
