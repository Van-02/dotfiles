"""
Pedir al usuario una frase. Determinar de al menos dos modos diferentes
 (con y sin listas) la cantidad de palabras que hay en dicha frase.
"""

# Without list
phrase = input("Please enter a phrase: ")

total = 0
for char in phrase:
    if char == " ":
        total += 1

print(f"The total words in the phrase is {total}")
# With list

words = phrase.split(" ")
print(f"The total words in the phrase is {len(words)}")
