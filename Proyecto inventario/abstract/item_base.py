from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, nombre, peso):
        self._nombre = nombre
        self._peso = peso

    @property
    def nombre(self):
        return self._nombre

    @abstractmethod
    def usar(self, objetivo):
        pass