"""
Dado un n ingresado por el usuario, realizar la suma de los n primeros 
terminos de la serie a continuacion. Mostrar el resultado.

1/1 + 1/2 + 1/3 + 1/4 + ... 1/n
"""

n_terms = int(input("Enter the number of terms for the series:"))
total_sum = 0

for i in range(1, n_terms + 1):
    total_sum += 1 / i

# Displaying the result with 4 decimal places for better precision
print(f"The sum of the first {n_terms} terms is: {total_sum:.4f}")
