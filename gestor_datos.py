import json
import os

class GestorJSON:
    def __init__(self, nombre_archivo="granja.json"):
        # Esto busca la carpeta exacta de tu proyecto en VS Code para no perder el JSON
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        self.__ruta_completa = os.path.join(directorio_actual, nombre_archivo)

    def guardar_datos(self, lista_diccionarios: list):
        try:
            # Abre o crea el archivo en modo escritura ('w')
            with open(self.__ruta_completa, 'w', encoding='utf-8') as archivo:
                json.dump(lista_diccionarios, archivo, indent=4, ensure_ascii=False)
            
            print(f"\n[ÉXITO]: Datos guardados correctamente en JSON.")
            print(f"Ubicación: {self.__ruta_completa}")
            
        except IOError as error:
            print(f"[ERROR CRÍTICO]: No se pudo escribir en el disco: {error}")
