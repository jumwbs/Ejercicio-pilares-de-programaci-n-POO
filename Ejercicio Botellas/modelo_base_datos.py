class BaseDatos:
    def __init__(self):
        self.lista_botellas = []

    def agregar_final_lista(self, nueva_botella):
        self.lista_botellas.append(nueva_botella)
        print("Botella agregada al final de la lista.")

    def modificar_atributo(self):
        if not self.lista_botellas:
            print("La lista está vacía.")
            return
        
        self.imprimir_info()
        pos = int(input("Ingrese la posición de la botella a modificar: ")) - 1
        if 0 <= pos < len(self.lista_botellas):
            atributo = input("Ingrese el atributo a modificar: ")
            valor = input("Ingrese el nuevo valor: ")
            setattr(self.lista_botellas[pos], atributo, valor)
            print("Atributo modificado correctamente.")
        else:
            print("Posición inválida.")

    def insertar_elemento_posicion(self, posicion, botella):
        if posicion < 0 or posicion > len(self.lista_botellas):
            print("Posición inválida.")
        else:
            self.lista_botellas.insert(posicion, botella)
            print("Botella insertada correctamente.")

    def eliminar_primer_elemento(self):
        if self.lista_botellas:
            self.lista_botellas.pop(0)
            print("Primer elemento eliminado.")
        else:
            print("La lista está vacía.")

    def eliminar_elemento_posicion(self, posicion):
        if 0 <= posicion < len(self.lista_botellas):
            self.lista_botellas.pop(posicion)
            print("Elemento eliminado correctamente.")
        else:
            print("Posición inválida.")

    def devolver_elemento_si_coincide(self, material):
        encontrados = [b for b in self.lista_botellas if b.material.lower() == material.lower()]
        if encontrados:
            for botella in encontrados:
                botella.mostrar_info()
                print("---")
        else:
            print(f"No hay botellas de material '{material}'.")

    def contar_numero_veces(self, material):
        contador = sum(1 for b in self.lista_botellas if b.material.lower() == material.lower())
        print(f"Hay {contador} botella(s) de {material}.")

    def ordenar_elementos_lista(self):
        self.lista_botellas.sort(key=lambda b: b.material)
        print("Lista ordenada por material.")

    def invertir_orden(self):
        self.lista_botellas.reverse()
        print("Orden invertido.")

    def imprimir_info(self):
        if not self.lista_botellas:
            print("La lista está vacía.")
            return
        for i, botella in enumerate(self.lista_botellas, 1):
            print(f"\n--- Botella {i} ---")
            botella.mostrar_info()