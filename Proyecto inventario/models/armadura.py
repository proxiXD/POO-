from abstract.item_base import Item
from interfaces.equipable import Equipable

class Armadura(Item, Equipable):
    def __init__(self, nombre, peso, defensa):
        super().__init__(nombre, peso)
        self._defensa = defensa

    @property
    def defensa(self):
        return self._defensa

    def usar(self, objetivo):
        print("La armadura no se usa directamente")

    def equipar(self, jugador):
        jugador.defensa += self._defensa

    def desequipar(self, jugador):
        jugador.defensa -= self._defensa