"""
Pedirle al usuario la cantidad de notas que desea ingresar. Luego pedir cada 
nota, y guardarlas.
"""

num_of_grades = int(input("Please, enter the number of grades: "))
grades = []

for i in range(num_of_grades):
    current_grade = int(input(f"Enter the grade {i + 1}: "))
    grades.append(current_grade)

print(f"List of grades: {grades}")
