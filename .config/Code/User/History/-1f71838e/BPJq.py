"""
Dada una lista de numeros, ingresada por el usuario o inventada por usted, 
cree otra lista con la cantidad de digitos de cada numero de la misma.
"""
numbers = [1, 21, 342, 4, 10000]
digit_counts = []

for num in numbers:
    digit_counts.append(len(str(num)))

print(digit_counts)
