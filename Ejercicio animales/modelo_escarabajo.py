from modelo_animal import Animal

class Escarabajo(Animal):
    def __init__(self):
        super().__init__(
            nombre="Escarabajo",
            edad=1,
            habitat="Bosques y campos",
            dieta="Detritívoro",
            tamaño="Muy pequeño",
            color="Negro"
        )

    # Métodos únicos
    def volar(self):
        print("El escarabajo puede volar cortas distancias.")

    def excavar(self):
        print("El escarabajo excava para esconderse.")

    def rodar_bolas(self):
        print("El escarabajo roda bolas de desechos como alimento.")
