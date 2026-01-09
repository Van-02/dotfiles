"""
El usuario podra ingresar nombre y apellido. El programa debera convertir 
las iniciales en mayusculas y las demas letras en minusculas.
"""

name = input("Ingrese su nombre: ")
surname = input("Ingrese su apellido: ")

print(name[0].upper() + name[1:].lower() + " " +
      surname[0].upper() + surname[1:].lower())
