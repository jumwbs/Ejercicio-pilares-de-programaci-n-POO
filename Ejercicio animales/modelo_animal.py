class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    # Métodos generales
    def moverse(self):
        print(f"{self.nombre} se está moviendo.")

    def comunicacion(self):
        print(f"{self.nombre} emite sonidos para comunicarse.")

    def reproduccion(self):
        print(f"{self.nombre} está en proceso de reproducción.")

    def alimentarse(self):
        print(f"{self.nombre} se está alimentando.")

    def adaptacion(self):
        print(f"{self.nombre} se adapta a su entorno.")

    def instintos(self):
        print(f"{self.nombre} sigue sus instintos naturales.")

    def descanso(self):
        print(f"{self.nombre} está descansando.")

    def sueño(self):
        print(f"{self.nombre} está durmiendo.")

    def interaccion_social(self):
        print(f"{self.nombre} interactúa con otros animales.")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Hábitat: {self.habitat}")
        print(f"Dieta: {self.dieta}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Color: {self.color}")
