
# Clase que representa el campo por donde se moverá nuestro borracho
class Campo:

    def __init__(self):
        self.coordenadas_de_borrachos = {}

    # Método que añade una nueva coordenada al diccionario de borrachos
    def anadir_borracho(self, borracho, coordenada):
        self.coordenadas_de_borrachos[borracho] = coordenada

    # Método que moverá a nuestro borracho
    def mover_borracho(self, borracho):
        # Retornara una tupla con la dirección
        delta_x, delta_y = borracho.camina()
        # Asignamos a la variable la coordenada actual de nuestro borracho
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenadas_de_borrachos[borracho] = nueva_coordenada

    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho]