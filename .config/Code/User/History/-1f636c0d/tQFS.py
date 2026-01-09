"""
Permitir ingresar 10 numeros al usuario. Determinar y mostrar el menor y 
el mayor
"""

max_num = None
min_num = None

print("Please, enter 10 numbers")
for _ in range(10):
    user_input = int(input("-> "))
    if max_num == None and min_num == None:
        max_num, min_num = user_input, user_input
    elif user_input > max_num:
        max_num = user_input
    elif user_input < min_num:
        min_num = user_input
