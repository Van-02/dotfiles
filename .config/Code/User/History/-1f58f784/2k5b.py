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
    print(f"The range of numbers is: {numbers}")

    random_number = random.choice(numbers)
    lives = 10
    has_won = False

    print("I have picked a number. Can you guess it?")

    while lives > 0:
        print(f"\nLives: {lives}")
        guess = int(input("Try to guess the number: "))

        if guess == random_number:
            print("Congratulations!! You guessed it")
            break
        else:
            lives -= 1

    if lives == 0:
        print(f"Game Over, the correct number is {random_number}")
