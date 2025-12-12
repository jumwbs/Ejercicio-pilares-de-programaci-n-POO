class Botella:
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseño = diseño
        self.tapa = tapa
        self.grabados = grabados

    # Métodos generales
    def contener_liquidos(self):
        print("Puede contener líquidos sin derramarse.")

    def facilitar_vertido(self):
        print("Facilita el vertido del contenido.")

    def cierre_hermetico(self):
        print("Tiene un cierre hermético para conservar el contenido.")

    def mostrar_info(self):
        print(f"Material: {self.material}")
        print(f"Capacidad: {self.capacidad} ml")
        print(f"Forma: {self.forma}")
        print(f"Diseño: {self.diseño}")
        print(f"Tapa: {self.tapa}")
        print(f"Grabados: {self.grabados}")
