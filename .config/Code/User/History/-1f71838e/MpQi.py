"""
Dada una lista de numeros, ingresada por el usuario o inventada por usted, 
cree otra lista con la cantidad de digitos de cada numero de la misma.
"""
numbers_list = [1, 21, 342, 4, 10000]
count_digits = []

for i in numbers_list:
    count_digits.append(len(str(i)))

print(count_digits)
