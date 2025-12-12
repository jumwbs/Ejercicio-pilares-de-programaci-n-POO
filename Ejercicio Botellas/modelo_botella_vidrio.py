from modelo_botella import Botella

class BotellaVidrio(Botella):
    def __init__(self):
        super().__init__(
            material="Vidrio",
            capacidad=750,
            forma="Recta",
            diseño="Verde oscuro",
            tapa="Corcho",
            grabados="Logo grabado en relieve"
        )

    def reciclar(self):
        print("La botella de vidrio puede reciclarse indefinidamente.")

    def enfriar(self):
        print("Mantiene las bebidas frías por más tiempo.")

    def romperse(self):
        print("El vidrio puede romperse fácilmente si cae.")