# 1. Importamos la clase base desde el archivo animal.py
from animal import Animal

# 2. Heredamos de Animal pasándolo entre paréntesis
class Gato(Animal):
    def __init__(self, nombre: str, edad: int, color_pelaje: str):
        # 3. Mandamos los datos obligatorios al constructor de la clase base
        super().__init__(nombre, edad)
        # 4. Agregamos el atributo exclusivo de esta subclase
        self.__color_pelaje = color_pelaje

    # 5. Cumplimos el contrato implementando el método obligatorio
    def hablar(self):
        print("¡Miau!")

    def convertir_a_diccionario(self) -> dict:
        return {
            "especie": "Gato",
            "nombre": self.obtener_nombre(),
            "edad": self.obtener_edad(),
            "color_pelaje": self.__color_pelaje
        }
