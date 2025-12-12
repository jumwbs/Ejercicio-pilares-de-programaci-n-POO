class BaseDatos2:
    def __init__(self):
        self.lista_vehiculos =[]
        
    def agregar_final_lista(self, nuevo_vehiculo):
        self.lista_vehiculos.append(nuevo_vehiculo)
        print("Vehiculo agregado al final de la lista.")

    def modificar_atributo(self):
        if not self.lista_vehiculos:
            print("La lista está vacía.")
            return
        
        self.imprimir_info()
        pos = int(input("Ingrese la posición del vehiculo a modificar: ")) - 1
        if 0 <= pos < len(self.lista_vehiculo):
            atributo = input("Ingrese el atributo a modificar: ")
            valor = input("Ingrese el nuevo valor: ")
            setattr(self.lista_vehiculos[pos], atributo, valor)
            print("Atributo modificado correctamente.")
        else:
            print("Posición inválida.")

    def insertar_elemento_posicion(self, posicion, vehiculo):
        if posicion < 0 or posicion > len(self.lista_vehiculos):
            print("Posición inválida.")
        else:
            self.lista_vehiculos.insert(posicion, vehiculo)
            print("Botella insertada correctamente.")

    def eliminar_primer_elemento(self):
        if self.lista_vehiculos:
            self.lista_vehiculos.pop(0)
            print("Primer elemento eliminado.")
        else:
            print("La lista está vacía.")

    def eliminar_elemento_posicion(self, posicion):
        if 0 <= posicion < len(self.lista_vehiculos):
            self.lista_vehiculos.pop(posicion)
            print("Elemento eliminado correctamente.")
        else:
            print("Posición inválida.")

    def devolver_elemento_si_coincide(self, modelo):
        encontrados = [b for b in self.lista_vehiculos if b.modelo.lower() == modelo.lower()]
        if encontrados:
            for botella in encontrados:
                botella.mostrar_info()
                print("---")
        else:
            print(f"No hay vehiculos de este modelo '{modelo}'.")

    def contar_numero_veces(self, modelo):
        contador = sum(1 for b in self.lista_vehiculos if b.modelo.lower() == modelo.lower())
        print(f"Hay {contador} vehiculo(s) de {modelo}.")

    def ordenar_elementos_lista(self):
        self.lista_vehiculos.sort(key=lambda b: b.modelo)
        print("Lista ordenada por modelo.")

    def invertir_orden(self):
        self.lista_vehiculo.reverse()
        print("Orden invertido.")

    def imprimir_info(self):
        if not self.lista_vehiculos:
            print("La lista está vacía.")
            return
        for i, vehiculo in enumerate(self.lista_vehiculos, 1):
            print(f"\n--- vehiculos {i} ---")
            vehiculo.mostrar_info()