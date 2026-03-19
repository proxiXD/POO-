from abstract.item_base import Item
from interfaces.equipable import Equipable

class Arma(Item, Equipable):
    def __init__(self, nombre, peso, dano):
        super().__init__(nombre, peso)
        self._dano = dano
        self._equipada = False

    def usar(self):
        print(f"Atacas con {self._nombre} y haces {self._dano} de daño")

    def equipar(self):
        self._equipada = True
        print(f"{self._nombre} equipada")

    def desequipar(self):
        self._equipada = False
        print(f"{self._nombre} desequipada")