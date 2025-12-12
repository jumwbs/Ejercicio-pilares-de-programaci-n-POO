from modelo_animal import Animal

class Pez(Animal):
    def __init__(self):
        super().__init__(
            nombre="Pez",
            edad=1,
            habitat="Océanos o ríos",
            dieta="Omnívoro",
            tamaño="Pequeño",
            color="Plateado"
        )

    # Métodos únicos
    def nadar(self):
        print("El pez nada rápidamente entre las corrientes.")

    def formar_banco(self):
        print("El pez se une a un banco para protegerse.")

    def respirar_brangias(self):
        print("El pez respira utilizando sus branquias.")
