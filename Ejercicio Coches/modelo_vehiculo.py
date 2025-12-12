## CLASE PADRE
# definimos los atributos comunes
class Vehiculo:
    def __init__(self):
        self.modelo =""
        self.color= ""
        self.motor=""
        self.num_puertas= 0
        self.capacidad_pasajeros= 0
        self.tipo_combustible=""
        
    # Método para asignar los atributos
    def asignar_caracteristicas (self, modelo ,color ,motor ,num_puertas ,capacidad_pasajeros , tipo_combustible):
        self.modelo = modelo
        self.color= color
        self.motor= motor
        self.num_puertas= num_puertas
        self.capacidad_pasajeros= capacidad_pasajeros
        self.tipo_combustible= tipo_combustible
        
        print(f"Vehiculo modelo {self.modelo}, color {self.color}, motor {self.motor},"
              f"{self.num_puertas} puertas, capacidad para {self.capacidad_pasajeros},"
              f"combustible {self.tipo_combustible}")
    
# Métodos generales (todos los vehículos los tienen)
    def arranque (self):
        print("El vehiculo ah frenado")
    def apagado (self):
        print("El vehiculo esta apagado")
    def aceleracion_frenado (self):
        print("El vehiculo acelera y frena correctamente")
    def sistema_direccion(self):
        print("El sistema de direccion esta activo")
    def climatizacion(self):
        print("El sistema de climatizacion esta activado")
    def tipo_seguridad(self):
        print("Tiene frenos ABS y airbags de seguridad")
    def luces(self):
        print("Las luces funcionan correctamente")
    def sistema_ventanas(self):
        print("Las ventanas electricas estan funcionando")
    def sistema_espejos(self):
        print("Los espejos retrovisores estan ajustados")    