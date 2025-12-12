from modelo_animal import Animal

class Cocodrilo(Animal):
    def __init__(self):
        super().__init__(
            nombre="Cocodrilo",
            edad=12,
            habitat="Ríos y pantanos",
            dieta="Carnívoro",
            tamaño="Grande",
            color="Verde oscuro"
        )

    # Métodos únicos
    def morder(self):
        print("El cocodrilo muerde con una fuerza increíble.")

    def nadar_sigiloso(self):
        print("El cocodrilo nada sin ser visto.")

    def tomar_sol(self):
        print("El cocodrilo toma el sol para regular su temperatura.")
