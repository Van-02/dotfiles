"""
Pedirle al usuario dos numeros positivos, a y b. Controlar que a < b. 
Mostrar en pantalla los numeros del intervalo cerrado [a, b] La computadora 
debera ahora seleccionar al azar un numero de ese intervalo. Y el usuario debera 
adivinar cual numero ha sido seleccionado por la computadora, obteniendo un 
mensaje de  ́exito en caso de acertar. El usuario solo tendra 10 vidas 
(numero de intentos) y en caso de no acertar, debera obtener un mensaje
de pucha
"""
import random

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a < b:
    numbers = list(range(a, b + 1))
    random_number = numbers[random.randint(0, len(numbers))]
    lives = 10

    print(f"Numbers: {numbers}")

    while lives != 0:
        print(f"Lives: {lives}")
        user_input = input("Try to guess the number: ")

        if user_input == random_number:
            print("Congratulations!! You're guessed")

    if lives == 0:
        print(f"You are losed, the correct number is {random_number}")
