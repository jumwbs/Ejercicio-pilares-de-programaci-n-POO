from modelo_vehiculo import Vehiculo

#CLASE HIJA 1
class Carro:
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
        
    def techo_corredizo(self):
        print(f"{self.modelo} tiene techo corredizo.")

    def modo_deportivo(self):
        print(f"{self.modelo} cuenta con un modo deportivo.")

    def asistente_estacionamiento(self):
        print(f"{self.modelo} tiene asistente para estacionar.")

    def mostrar_info(self):
        print(f"Carro - Modelo: {self.modelo}, Color: {self.color}, Motor: {self.motor}, Puertas: {self.puertas}, Asientos: {self.asientos}, Combustible: {self.combustible}")