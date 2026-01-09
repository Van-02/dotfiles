"""
Se deberan ingresar 8 notas. Se mostrara el promedio, redondeado a 2 decimales.
"""

grades = []

print("Please enter 8 grades: ")

for i in range(8):
    grade = int(input(f"Grade {i + 1} ->  "))
    grades.append(grade)

total_sum = sum(grades)

average = total_sum / len(grades)


print(f"The average of all grades is: {round(average, 2)}")
