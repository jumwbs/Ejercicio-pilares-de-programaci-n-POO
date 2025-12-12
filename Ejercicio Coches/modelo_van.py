from modelo_vehiculo import Vehiculo

#CLASE HIJA 2
class Van:
    def __init__(self):
        self.modelo = ""
        self.color = ""
        self.motor = ""
        self.puertas = 0
        self.asientos = 0
        self.combustible = ""

    def asignar_caracteristicas(self, modelo, color, motor, puertas, asientos, combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.puertas = puertas
        self.asientos = asientos
        self.combustible = combustible
        
    def puertas_laterales(self):
        print(f"{self.modelo} tiene puertas que abren lateralmente.")

    def asientos_reclinables(self):
        print(f"{self.modelo} tiene asientos reclinables.")

    def espacio_equipaje(self):
        print(f"{self.modelo} tiene un amplio espacio de equipaje.")

    def mostrar_info(self):
        print(f"Van - Modelo: {self.modelo}, Color: {self.color}, Motor: {self.motor}, Puertas: {self.puertas}, Asientos: {self.asientos}, Combustible: {self.combustible}")