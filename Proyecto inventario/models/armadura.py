from abstract.item_base import Item
from interfaces.equipable import Equipable

class Armadura(Item, Equipable):
    def _init_(self, nombre, peso, defensa):
        super()._init_(nombre, peso)
        self._defensa = defensa
        self._equipada = False

    def usar(self):
        print(f"La armadura {self._nombre} no se usa directamente")

    def equipar(self):
        self._equipada = True
        print(f"{self._nombre} equipada")

    def desequipar(self):
        self._equipada = False
        print(f"{self._nombre} desequipada")
