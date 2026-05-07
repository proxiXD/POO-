from abc import ABC, abstractmethod

class Equipable(ABC):

    @abstractmethod
    def equipar(self, jugador):
        pass

    @abstractmethod
    def desequipar(self, jugador):
        pass