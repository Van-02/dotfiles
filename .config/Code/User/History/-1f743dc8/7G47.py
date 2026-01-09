"""
Implemente el programa que pide al usuario 8 nombres del algoritmo del 
practico anterior. En ese ejercicio tenia que intentar diseñar un algoritmo que 
seleccionase los nombres que empiezan con la letra M de una serie de nombres 
otorgados por el usuario. Utilice para resolverlo los tipos de datos y comandos 
que le parezcan mas apropiados
"""

namesdb = ["Jinx", "Vi", "Caitlyn", "Jayce",
           "Ambessa", "Mel", "Viktor", "Warwick", "Mireia"]

for name in namesdb:
    if name[0] == "M" or name[0] == "m":
        print(name)
