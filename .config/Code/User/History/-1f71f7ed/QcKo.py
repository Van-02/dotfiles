"""
Pedir al usuario una frase. Determinar de al menos dos modos diferentes
 (con y sin listas) la cantidad de palabras que hay en dicha frase.
"""

# Without list
phrase = input("Please enter a phrase: ")

word_count = 0
for char in phrase:
    if char == " ":
        word_count += 1

print(f"The total words in the phrase is {word_count}")
# With list

words = phrase.split(" ")
print(f"The total words in the phrase is {len(words)}")
