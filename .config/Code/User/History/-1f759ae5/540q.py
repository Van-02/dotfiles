"""
Permitir ingresar al usuario un numero de un digito. Controlando se haya 
ingresado dicho numero de no mas de 1 digito de longitud, pasarlo a letras y 
mostrarlo en pantalla. (Ejemplo: Si ingresa 3, se vera como resultado ”tres”).
"""

number = int(input("Ingrese un numero: "))

if number < 0 or number > 9:
    print("Numero incorrecto")

elif number == 0:
    print("cero")

elif number == 1:
    print("uno")

elif number == 2:
    print("dos")

elif number == 3:
    print("tres")

elif number == 4:
    print("cuatro")

elif number == 5:
    print("cinco")

elif number == 6:
    print("seis")

elif number == 7:
    print("siete")

elif number == 8:
    print("ocho")

elif number == 9:
    print("nueve")
