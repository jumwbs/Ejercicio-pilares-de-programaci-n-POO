from modelo_animal import Animal

class Caballo(Animal):
    def __init__(self):
        super().__init__(
            nombre="Caballo",
            edad=5,
            habitat="Praderas",
            dieta="Herbívoro",
            tamaño="Grande",
            color="Café"
        )

    # Métodos únicos
    def galopar(self):
        print("El caballo galopa a gran velocidad.")

    def relinchar(self):
        print("El caballo relincha fuertemente.")

    def tirar_carro(self):
        print("El caballo puede tirar de un carro o carreta.")
