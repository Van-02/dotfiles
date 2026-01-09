"""
Pedirle al usuario la cantidad de notas que desea ingresar. Luego pedir cada 
nota, y guardarlas.
"""

grades_count = int(input("Please, enter the amount of grades: "))
grades = []

for grade in range(grades_count):
    grade = input(f"Enter the grade {grade}: ")
    grades.append(grade)
