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

class ReglaCifradoTraslacion(ReglaCifrado):
    def __init__(self):
        super().__init__()

    def mensaje_valido(self, mensaje: str) -> bool:
        if mensaje in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False

        if mensaje == " " or mensaje in "@_#$o%":
            return False

        for letras in mensaje:
            if letras not in string.ascii_lowercase:
                return False

        return True

    def encriptar(self, mensaje: str) -> str:

        mensaje_encriptado = ""

        for caracter in mensaje:
            x = mensaje.index(caracter)

    def desencriptar(self, mensaje: str) -> str:
        pass

class ReglaCifradoNumerico(ReglaCifrado):
    def __init__(self):
        super().__init__()

    def mensaje_valido(self, mensaje: str) -> bool:
        if mensaje in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False

        if mensaje[0] == " " or mensaje[len(mensaje)] == " ":
            return False

        contador_espacios = 0
        hay_espacio = False
        for caracteres in mensaje:
            if caracteres == " ":
                contador_espacios += 1
                hay_espacio = True

            #TODO: Continuar...


    def encriptar(self, mensaje: str) -> str:
        pass

    def desencriptar(self, mensaje: str) -> str:
        pass























