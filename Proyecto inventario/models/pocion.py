Item = str
class Pocion(Item):
    def __init__(self, nombre, peso, curacion):
        super()._init_(nombre, peso)
        self._curacion = curacion

    def usar(self):
        print(f"Recuperas {self._curacion} puntos de vida")