from abc import ABC, abstractmethod

class Subjet(ABC):
    def __init__(self):
        self._observateurs = []

    def abonner(self, observateur) -> None:
        self._observateurs.append(observateur)

    def desabonner(self, observateur) -> None:
        self._observateurs.remove(observateur)

    def notifier(self) -> None:
        pass