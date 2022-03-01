import random

class Borracho:

    def __init__(self, nombre):
        self.nombre = nombre


# Subclase de Borracho
class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    # Método que utilizaremos para escoger a que dirección caminara el borracho
    # Izquierda, Derecha, Arriba, Abajo
    def camina(self):
        return random.choice([(-1, 0), (1, 0), (0, 1), (0, -1)])