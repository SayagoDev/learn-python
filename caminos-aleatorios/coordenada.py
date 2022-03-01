
# Clase que nos proporcionara la abstracción de movimiento en el campo
class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Método que retorna una nueva instancia de Coordenada con los
    # valores actualizados, despues de que nuestro borracho caminara
    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)

    # Método que retorna la distancia entre una coordenada y otra
    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y

        return (delta_x**2 + delta_y**2)**0.5