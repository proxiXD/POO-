from systems.inventario import Inventario
from interfaces.equipable import Equipable

class Jugador:
    def __init__(self, nombre, vida_maxima=100):
        self._nombre = nombre
        self._vida_maxima = vida_maxima
        self._vida = vida_maxima
        self.inventario = Inventario()
        self._equipamiento = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def vida(self):
        return self._vida

    def curar(self, cantidad):
        self._vida += cantidad
        if self._vida > self._vida_maxima:
            self._vida = self._vida_maxima

    def equipar_item(self, item):
        if isinstance(item, Equipable):
            item.equipar(self)
            self._equipamiento.append(item)
        else:
            print(f" {item.nombre} no se puede equipar.")
