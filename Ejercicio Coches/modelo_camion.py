from modelo_vehiculo import Vehiculo
class Camion:
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
        
    def carga_pesada(self):
        print(f"{self.modelo} tiene la capacidad de carga pesada.")

    def frenos_neumaticos(self):
        print(f"{self.modelo} tiene frenos neumáticos.")

    def remolque_acoplado(self):
        print(f"{self.modelo} tiene un remolque acoplado.")

    def mostrar_info(self):
        print(f"Camión - Modelo: {self.modelo}, Color: {self.color}, Motor: {self.motor}, Puertas: {self.puertas}, Asientos: {self.asientos}, Combustible: {self.combustible}")