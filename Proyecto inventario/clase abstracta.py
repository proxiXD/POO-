from abc import ABC, abstractmethod

class Item(ABC):
    def _init_(self, nombre, peso):
        self._nombre = nombre      # encapsulado
        self._peso = peso

    def get_nombre(self):
        return self._nombre

    def get_peso(self):
        return self._peso

    @abstractmethod
    def usar(self):
        pass