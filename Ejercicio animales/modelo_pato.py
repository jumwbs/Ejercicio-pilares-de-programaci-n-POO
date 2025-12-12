from modelo_animal import Animal

class Pato(Animal):
    def __init__(self):
        super().__init__(
            nombre="Pato",
            edad=2,
            habitat="Lagos",
            dieta="Omnívoro",
            tamaño="Mediano",
            color="Blanco"
        )

    # Métodos únicos
    def graznar(self):
        print("El pato grazna fuertemente.")

    def volar_corto(self):
        print("El pato vuela a baja altura por distancias cortas.")

    def nadar_con_patas(self):
        print("El pato utiliza sus patas palmeadas para nadar.")
