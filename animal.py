from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre
        self.__edad = edad

    def obtener_nombre(self) -> str:
        return self.__nombre

    def obtener_edad(self) -> str:
        return self.__edad

    @abstractmethod
    def hablar(self):
        pass
