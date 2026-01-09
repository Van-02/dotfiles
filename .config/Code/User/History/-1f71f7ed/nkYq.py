"""
Pedir al usuario una frase. Determinar de al menos dos modos diferentes
 (con y sin listas) la cantidad de palabras que hay en dicha frase.
"""

# --- Method 1: Without lists (Counting spaces) ---
phrase = input("Please enter a phrase: ")

if not phrase:
    word_count_no_list = 0
else:
    word_count_no_list = 1
    for char in phrase:
        if char == " ":
            word_count_no_list += 1

print(f"Method 1 - Word count: {word_count_no_list}")

# --- Method 2: With lists (Using split) ---
words = phrase.split(" ")
print(f"The total words in the phrase is {len(words)}")
