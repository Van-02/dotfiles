"""
Realizar un procedimiento que tome como parametro una longitud e imprima en 
pantalla un rectangulo de numerales, hueco por dentro. Por ejemplo, si se 
ingreso 4, se vera en pantalla: 

####
#  #
#  #
####

Tip: Puede ser util pensarlo por linea horizontal

Generalizarlo, luego, en una version 2, para un parametro extra: el caracter que 
se usara para dibujar el rectangulo, en vez de usar siempre un numeral.
"""


def rectangle(lenght: int, character: str) -> None:
    for i in range(lenght):
        if i == 0 or i == lenght - 1:
            print(character * lenght)
        else:
            spaces = " " * (lenght - 2)
            print(f"{character}{spaces}{character}")


rectangle(10, "*")
