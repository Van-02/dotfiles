"""
Implementar un programa que le permita al usuario ingresar su dia y mes de
nacimiento (no la fecha, solo el dia, controlando que este entre 1 y 31) y el
mes de nacimiento (como texto, enero, febrero, etc) y determine que signo 
zodiacal es.
"""

day = int(input("Ingrese su dia de nacimiento: "))
month = input("Ingrese su mes de nacimiento: ")
january = "enero"
february = "febrero"
march = "marzo"
april = "abril"
may = "mayo"
june = "junio"
july = "julio"
august = "agosto"
september = "septiembre"
october = "octubre"
november = "noviembre"
december = "diciembre"

if day > 31:
    print("Ingrese un dia entre 1 y 31")

if month == march and day >= 21 or month == april and day <= 19:
    print("Tu signo es Aries")
