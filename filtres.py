from abc import abstractmethod, ABC
import numpy as np


class AbstractFiltre(ABC):
    def __init__(self, nom: str):
        self._nom = nom
        self._parametres = {}


    @abstractmethod
    def filtrer(self, signal: list[float], frequence: int) -> list[float]:
        raise NotImplementedError("La méthode filtrer doit être implémentée par les sous-classes.")

    def __str__(self) -> str:
        return f"Filtre: {self.nom}"

   # TODO Ajouter les getters et setters pour nom et parametres

class ReverberationFiltre(AbstractFiltre):
    def __init__(self, nom: str, attenuation: float, delay_ms: int):
        pass

    def filtrer(self, signal: list[float], frequence: int) -> list[float]:
        pass


class PasseBasFiltre(AbstractFiltre):

    def __init__(self, nom: str, frequence_coupure: float):
        pass

    def filtrer(self, signal: list[float], frequence: int) -> list[float]:
        pass


class PasseHautFiltre(AbstractFiltre):
    def __init__(self, nom: str, frequence_coupure: float):
        pass


    def filtrer(self, signal: list[float], frequence: int) -> list[float]:
        pass
