"""
Implementar un programa que le permita al usuario ingresar su dia y mes de
nacimiento (no la fecha, solo el dia, controlando que este entre 1 y 31) y el
mes de nacimiento (como texto, enero, febrero, etc) y determine que signo 
zodiacal es.
"""

day = int(input("Ingrese su dia de nacimiento: "))
month = input("Ingrese su mes de nacimiento: ")
months = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
          "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

if day > 31:
    print("Ingrese un dia entre 1 y 31")
