from abc import ABC, abstractmethod

class Equipable(ABC):

    @abstractmethod
    def equipar(self):
        pass

    @abstractmethod
    def desequipar(self):
        pass
