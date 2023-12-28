import datetime
"""
Modelar el objeto Amigo. Además, de la información básica que representa a un amigo, 
su apellido, apodo, nombre, celular, cumple, entorno (entorno representará de donde 
se conoce a dicha persona, y podrá ser alguna de estas opciones trabajo, facultad, escuela, 
infancia, hobby, otro) deberá tener un modo de devolver cuantos años tiene.

Recuerde modelar bien el objeto, incluso para poder hacer un print del mismo y 
que muestre los datos correspondientes, de buen modo.
"""


class Amigo:
    def __init__(self, apellido, apodo, nombre, celular, cumple, entorno):
        self.apellido = apellido
        self.apodo = apodo
        self.nombre = nombre
        self.celular = celular
        self.cumple = cumple
        self.entorno = entorno

    def edad(self):
        pass


hoy = datetime.datetime.today()
anio = hoy.year

print(anio)
