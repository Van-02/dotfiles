"""
Realice un programa que informe el valor total en pesos de una transaccion en 
dolares. Para ello, el programa debe leer el monto total en dolares de la 
transaccion, el valor del dolar del dia de la fecha y el porcentaje (en pesos)
de la comision que cobra el banco por la transaccion. Por ejemplo, si la 
transaccion se realiza por 10 dolares, el dolar tiene un valor de 20,54 pesos y
el banco cobra un 4% de comision, entonces el programa debera informar: 
La transaccion sera de 213.61 pesos argentinos (resultado de multplicar 
10 * 20.54 y adicionarle el 4%)
"""

dolar_mount = float(
    input("Ingrese el monto total en dolares de la transaccion: "))
dolar_value = 20.54
comission = (dolar_mount * dolar_value) * 0.04

print(comission)
print(
    f"La transaccion sera de {dolar_mount * dolar_value + comission} pesos argentinos")
