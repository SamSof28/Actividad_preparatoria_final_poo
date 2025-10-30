import string
from abc import ABC, abstractmethod

class ReglaCifrado(ABC):
    def __init__(self, token: int):
        self.token: int = token

    @abstractmethod
    def mensaje_valido(self, mensaje: str) -> bool:
        pass

    @abstractmethod
    def encriptar(self, mensaje: str) -> str:
        pass

    @abstractmethod
    def desencriptar(self, mensaje: str) -> str:
        pass

    def encontrar_numeros_mensaje(self, mensaje: str) -> list:
        pass

    def encontrar_no_ascii_mensaje(self, mensaje: str) -> list:
        pass










