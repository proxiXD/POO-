from abstract.item_base import Item
from interfaces.equipable import Equipable

class Arma(Item, Equipable):
    def __init__(self, nombre, peso, dano, tipo):
        super().__init__(nombre, peso)
        self._dano = dano
        self._tipo = tipo
        self._equipada = False

    @property
    def dano(self):
        return self._dano

    @property
    def tipo(self):
        return self._tipo

    def usar(self, objetivo):
        print(f"Atacas con {self._nombre}")
        objetivo.recibir_dano(self._dano)

    def equipar(self, jugador):
        self._equipada = True
        jugador.agregar_equipo(self)

    def desequipar(self, jugador):
        self._equipada = False
