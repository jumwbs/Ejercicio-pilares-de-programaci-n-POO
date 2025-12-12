class BaseDatosAnimales:
    def __init__(self):
        self.lista_animales = []

    def agregar_final_lista(self, animal):
        self.lista_animales.append(animal)
        print("Animal agregado al final de la lista.")

    def insertar_elemento_posicion(self, posicion, animal):
        if posicion < 0 or posicion > len(self.lista_animales):
            print("Posición inválida.")
        else:
            self.lista_animales.insert(posicion, animal)
            print("Animal insertado correctamente.")

    def eliminar_primer_elemento(self):
        if self.lista_animales:
            self.lista_animales.pop(0)
            print("Primer elemento eliminado.")
        else:
            print("La lista está vacía.")

    def eliminar_elemento_posicion(self, posicion):
        if 0 <= posicion < len(self.lista_animales):
            self.lista_animales.pop(posicion)
            print("Elemento eliminado correctamente.")
        else:
            print("Posición inválida.")

    def buscar_por_nombre(self, nombre):
        encontrados = [a for a in self.lista_animales if a.nombre.lower() == nombre.lower()]
        if encontrados:
            for animal in encontrados:
                animal.mostrar_info()
                print("---")
        else:
            print(f"No hay animales con nombre '{nombre}'.")

    def contar_animales(self, nombre):
        contador = sum(1 for a in self.lista_animales if a.nombre.lower() == nombre.lower())
        print(f"Hay {contador} animal(es) de tipo {nombre}.")

    def ordenar_por_nombre(self):
        self.lista_animales.sort(key=lambda a: a.nombre)
        print("Lista ordenada por nombre.")

    def invertir_orden(self):
        self.lista_animales.reverse()
        print("Orden invertido.")

    def imprimir_info(self):
        if not self.lista_animales:
            print("La lista está vacía.")
            return
        for i, animal in enumerate(self.lista_animales, 1):
            print(f"\n--- Animal {i} ---")
            animal.mostrar_info()
