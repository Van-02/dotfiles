"""
Permitir ingresar 10 numeros al usuario. Determinar y mostrar el menor y 
el mayor
"""

max_num = None
min_num = None

print("Please enter 10 numbers")
for i in range(10):
    user_input = int(input(f"Number {i + 1} -> "))

    if max_num is None or min_num is None:
        max_num, min_num = user_input, user_input
    else:
        if user_input > max_num:
            max_num = user_input
        if user_input < min_num:
            min_num = user_input

print(f"Max number: {max_num}\nMin number: {min_num}")
