"""
Pida 10 nombres de peliculas al usuario. Guardelos en una lista. Luego pida 
al usuario que ingrese un numero n del 1 al 10. Controle que n este en el rango 
correcto, es decir entre 1 y 10. Muestre en pantalla cual es la pelicula n-esima.
Por ejemplo, si el usuario me ingresa 1, debo mostrar la primer pelicula de la 
lista.
"""
moviesdb = []

print("Ingrese 10 peliculas")

for movie in range(10):
    movie = input(" -> ")
    moviesdb.append(movie)

n = int(input("Ingrese un numero del 1 al 10: "))

if n < 1 or n > 10:
    print("Numero no valido")
