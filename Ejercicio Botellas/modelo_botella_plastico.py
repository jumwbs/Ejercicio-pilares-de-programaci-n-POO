from modelo_botella import Botella

class BotellaPlastica(Botella):
    def __init__(self):
        super().__init__(
            material="Plástico",
            capacidad=600,
            forma="Cilíndrica",
            diseño="Transparente",
            tapa="Rosca",
            grabados="Logo reciclable"
        )

    def aplastar(self):
        print("Puede aplastarse fácilmente para reciclarla.")

    def reutilizar(self):
        print("Puede reutilizarse varias veces antes de desecharla.")

    def derretir(self):
        print("El plástico se deforma si se expone a altas temperaturas.")