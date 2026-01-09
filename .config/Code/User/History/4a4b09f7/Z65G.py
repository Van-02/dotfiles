"""
Escriba una funcion denominada cuadrante(x, y), donde x e y son valores 
enteros recibidos como parametros los cuales representan un punto, y que retorne 
un valor entre 1, 2, 3 o 4 de acuerdo al cuadrante que se encuentre el punto 
(x, y), ingresado como parametro, en los ejes cartesianos.
"""


def quadrant(x, y):
    """
    Determines the quadrant of a point (x, y).

            |
        2   |   1
            |
    -----------------
            |
        3   |   4
            |

    Returns:
        1, 2, 3, or 4 for the respective quadrants.
        0 if the point is on an axis or at the origin.
    """

    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return 0


# Pruebas
print(f"Punto (5, 5) -> Cuadrante: {quadrant(5, 5)}")
print(f"Punto (-5, -5) -> Cuadrante: {quadrant(-5, -5)}")
print(f"Punto (0, 10) -> Cuadrante: {quadrant(0, 10)}")  # Caso de eje
