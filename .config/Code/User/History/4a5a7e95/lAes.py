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


def rectangle(lenght: int) -> None:
    for i in range(lenght):
        if i == 0:
            print("#" * lenght)
        elif i == lenght - 1:
            print("#" * lenght)
        else:
            print("#" + " " * (lenght - 2) + "#")


rectangle(10)
