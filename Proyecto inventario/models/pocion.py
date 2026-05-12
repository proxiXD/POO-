from abstract.item_base import Item

class Pocion(Item):
    def __init__(self, nombre, peso, curacion):
        super().__init__(nombre, peso)
        self._curacion = curacion

    def usar(self, objetivo):
        objetivo.curar(self._curacion)
        print(f"{objetivo.nombre} recupera {self._curacion} HP")