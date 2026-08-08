# 1. Importamos la subclase y el gestor de datos
from gato import Gato
from gestor_datos import GestorJSON

def main():
    print("=" * 60)
    print("   SISTEMA DE PERSISTENCIA - UPBC")
    print("=" * 60)

    # 2. Creamos el objeto Gato en la memoria RAM
    mi_gato = Gato("Garfield", 5, "Naranja")
    mi_gato2 = Gato("Con Botas", 3, "Azul") 
    
    # 3. Lo metemos en una lista (por si luego tienes más animales)
    lista_animales = [mi_gato, mi_gato2]
    datos_a_guardar = []
    
    # 4. Convertimos los objetos a diccionarios (Serialización)
    for animal in lista_animales:
        datos_a_guardar.append(animal.convertir_a_diccionario())

    # 5. Instanciamos el gestor y guardamos físicamente
    base_datos = GestorJSON()
    base_datos.guardar_datos(datos_a_guardar)
    
    print("=" * 60)

if __name__ == "__main__":
    main()
