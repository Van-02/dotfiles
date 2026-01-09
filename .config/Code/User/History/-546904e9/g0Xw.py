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

# Aries
if month == march and day >= 21 or month == april and day <= 19:
    print("Tu signo es Aries")

# Tauro
elif month == april and day >= 20 or month == may and day <= 20:
    print("Tu signo es Tauro")

# Geminis
elif month == may and day >= 21 or month == june and day <= 20:
    print("Tu signo es Geminis")

# Cancer
elif month == june and day >= 21 or month == july and day <= 22:
    print("Tu signo es Cancer")

# Leo
elif month == july and day >= 23 or month == august and day <= 22:
    print("Tu signo es Leo")

# Virgo
elif month == august and day >= 23 or month == september and day <= 22:
    print("Tu signo es Virgo")

# Libra
elif month == september and day >= 23 or month == october and day <= 22:
    print("Tu signo es Libra")

# Escorpio
elif month == october and day >= 23 or month == november and day <= 21:
    print("Tu signo es Escorpio")

# Sagitario
elif month == november and day >= 22 or month == december and day <= 21:
    print("Tu signo es Sagitario")

# Capricornio
elif month == december and day >= 22 or month == january and day <= 19:
    print("Tu signo es Capricornio")

# Acuario
elif month == january and day >= 20 or month == february and day <= 18:
    print("Tu signo es Acuario")

# Piscis
elif month == february and day >= 19 or month == march and day <= 20:
    print("Tu signo es Piscis")
