"""
Dada la siguiente lista de compras de ingredientes para preparar una torta, 
mostrarla en pantalla, un ingrediente por linea. Luego corregir el ultimo a 
"Canela en polvo"
["Chocolate", "Huevos", "Manteca", "Crema de leche", "Frutillas"]
"""

ingredients = ["Chocolate", "Huevos", "Manteca", "Crema de leche", "Frutillas"]

for i in ingredients:
    print(i)

ingredients[-1] = "Canela en polvo"

print(ingredients)
