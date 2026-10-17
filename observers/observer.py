from abc import ABC, abstractmethod

class Observer(ABC):
    
    @abstractmethod
    def actualiser(self, sujet) -> None:
        pass