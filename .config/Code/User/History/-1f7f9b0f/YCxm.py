"""
Permita al usuario ingresar el nombre de un archivo, genere un nuevo nombre 
donde los espacios sean reemplazados por guion bajo y la extension por numerales.
"""
import re
# 1. Solicitar el nombre al usuario
nombre_original = input("Ingresa el nombre del archivo: ")

# 2. Reemplazar espacios por guiones bajos
# Usamos el método .replace() que es el más directo para esto
nombre_con_guiones = nombre_original.replace(" ", "_")

# 3. Identificar y transformar la extensión usando Regex
# Buscamos el último punto y capturamos lo que sigue
patron = r"^(.*)\.(.*)$"
busqueda = re.search(patron, nombre_con_guiones)

if busqueda:
    base = busqueda.group(1)       # Todo lo que está antes del punto
    extension = busqueda.group(2)  # La extensión original (ej: "pdf")

    # Creamos una cadena de '#' con el mismo largo que la extensión
    numerales = "#" * len(extension)

    # Unimos las partes
    nombre_final = f"{base}.{numerales}"
else:
    # Si el archivo no tiene extensión, dejamos el nombre con guiones
    nombre_final = nombre_con_guiones

print(f"El nuevo nombre es: {nombre_final}")
