"""
Pedir una palabra al usuario. Mostrar en pantalla una nueva palabra que 
este formada por la primera letra, la letra del medio y la ultima letra. 
Por ejemplo, si se ingreso “patos“ se vera “pts“ y si se ingresa “zapato“ se vera 
“zao“.
"""

word = input("Ingrese una palabra: ")
new_word = word[0] + word[len(word) // 2] + word[-1]

print(f"La nueva palabra es: {new_word}")
