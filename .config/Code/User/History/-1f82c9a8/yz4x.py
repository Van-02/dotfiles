"""
Pedir una palabra al usuario y armar una nueva palabra que sea los tres 
caracteres del medio de la palabra ingresada.
"""

word = input("Ingrese una palabra: ")
new_word = word[len(word) // 2 - 1] + word[len(word) //
                                           2] + word[len(word) // 2 + 1]
