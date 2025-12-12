from modelo_base_datos import BaseDatos2
from modelo_camion import Camion
from modelo_carro import Carro
from modelo_van import Van

def menu():
    print("===== MENÚ DE VEHÍCULOS =====")
    print("1. Agregar vehículo al final de la lista (append)")
    print("2. Agregar vehículos de otra lista al final (extend)")
    print("3. Insertar vehículo en posición específica (insert)")
    print("4. Eliminar el primer vehículo (pop / remove)")
    print("5. Eliminar vehículo por posición (pop)")
    print("6. Buscar vehículo por modelo (index / filter)")
    print("7. Contar número de vehículos por el tipo (count)")
    print("8. Ordenar vehículos de la lista (sort)")
    print("9. Invertir el orden de la lista (reverse)")
    print("10. Imprimir información completa")
    print("11. Ver métodos específicos de un vehículo")
    print("0. Salir")

def mostrar_metodos_vehiculo(vehiculo):
    print(f"--- Métodos específicos de vehículo {vehiculo.modelo} ---")
    if isinstance(vehiculo, Camion):
        vehiculo.carga_pesada()
        vehiculo.frenos_neumaticos()
        vehiculo.remolque_acoplado()
    elif isinstance(vehiculo, Van):
        vehiculo.puertas_laterales()
        vehiculo.asientos_reclinables()
        vehiculo.espacio_equipaje()
    elif isinstance(vehiculo, Carro):
        vehiculo.techo_corredizo()
        vehiculo.modo_deportivo()
        vehiculo.asistente_estacionamiento()

def crear_lista_vehiculos():
    lista_temporal = []
    try:
        cantidad = int(input("¿Cuántos vehículos desea agregar? "))
    except ValueError:
        print("Número inválido.")
        return lista_temporal

    for i in range(cantidad):
        print(f"\nVehículo {i + 1}:")
        print("a) Camión")
        print("b) Van")
        print("c) Carro")
        modelo = input("Seleccione el modelo: ").lower()
        if modelo == "a":
            vehiculo = Camion()
        elif modelo == "b":
            vehiculo = Van()
        elif modelo == "c":
            vehiculo = Carro()
        else:
            print("Tipo no válido, se omite este vehículo.")
            continue
        # Asignar características aquí si es necesario
        lista_temporal.append(vehiculo)
    return lista_temporal

def main():
    bd = BaseDatos2()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nSeleccione el tipo de vehículo a agregar:")
            print("a) Camión")
            print("b) Van")
            print("c) Carro")
            tipo = input("Opción: ").lower()
            if tipo == "a":
                vehiculo = Camion()
            elif tipo == "b":
                vehiculo = Van()
            elif tipo == "c":
                vehiculo = Carro()
            else:
                print("Tipo no válido.")
                continue
            bd.agregar_final_lista(vehiculo)

        elif opcion == "2":
            lista_nueva = crear_lista_vehiculos()
            if lista_nueva:
                bd.lista_vehiculos.extend(lista_nueva)
                print(f"Se agregaron {len(lista_nueva)} vehículo(s) al final usando extend().")
            else:
                print("No se agregaron vehículos.")

        elif opcion == "3":
            try:
                pos = int(input("Ingrese la posición donde desea insertar el vehículo (1-based): ")) - 1
            except ValueError:
                print("Posición inválida.")
                continue
            print("\nSeleccione el tipo de vehículo a insertar:")
            print("a) Camión")
            print("b) Van")
            print("c) Carro")
            tipo = input("Opción: ").lower()
            if tipo == "a":
                vehiculo = Camion()
            elif tipo == "b":
                vehiculo = Van()
            elif tipo == "c":
                vehiculo = Carro()
            else:
                print("Tipo no válido.")
                continue
            bd.insertar_elemento_posicion(pos, vehiculo)

        elif opcion == "4":
            bd.eliminar_primer_elemento()

        elif opcion == "5":
            try:
                pos = int(input("Ingrese la posición del elemento a eliminar (1-based): ")) - 1
            except ValueError:
                print("Posición inválida.")
                continue
            bd.eliminar_elemento_posicion(pos)

        elif opcion == "6":
            modelo = input("Ingrese el modelo a buscar: ")
            bd.devolver_elemento_si_coincide(modelo)
            for i, b in enumerate(bd.lista_vehiculos):
                if b.modelo.lower() == modelo.lower():
                    print(f"Índice del primer elemento que coincide: {i + 1}")
                    break

        elif opcion == "7":
            tipo = input("Ingrese el tipo a contar: ")
            bd.contar_numero_veces(tipo)

        elif opcion == "8":
            bd.ordenar_elementos_lista()

        elif opcion == "9":
            bd.invertir_orden()

        elif opcion == "10":
            bd.imprimir_info()

        elif opcion == "11":
            if not bd.lista_vehiculos:
                print("La lista está vacía.")
            else:
                bd.imprimir_info()
                try:
                    pos = int(input("Ingrese la posición del vehículo para ver sus métodos específicos (1-based): ")) - 1
                except ValueError:
                    print("Posición inválida.")
                    continue
                if 0 <= pos < len(bd.lista_vehiculos):
                    mostrar_metodos_vehiculo(bd.lista_vehiculos[pos])
                else:
                    print("Posición inválida.")

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()