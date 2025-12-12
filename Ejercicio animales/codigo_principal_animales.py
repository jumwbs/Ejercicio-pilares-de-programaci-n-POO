from modelo_caballo import Caballo
from modelo_cocodrilo import Cocodrilo
from modelo_pez import Pez
from modelo_escarabajo import Escarabajo
from modelo_pato import Pato
from modelo_base_datos_animales import BaseDatosAnimales

def menu():
    print("\n===== MENÚ DE ANIMALES =====")
    print("1. Agregar animal al final de la lista")
    print("2. Insertar animal en posición específica")
    print("3. Eliminar primer elemento")
    print("4. Eliminar animal por posición")
    print("5. Buscar animal por nombre")
    print("6. Contar animales por tipo")
    print("7. Ordenar por nombre")
    print("8. Invertir lista")
    print("9. Mostrar información")
    print("10. Ver métodos únicos de un animal")
    print("0. Salir")

def mostrar_metodos_animal(animal):
    print(f"\n--- Métodos únicos de {animal.nombre} ---")

    if isinstance(animal, Caballo):
        animal.galopar()
        animal.relinchar()
        animal.tirar_carro()

    elif isinstance(animal, Cocodrilo):
        animal.morder()
        animal.nadar_sigiloso()
        animal.tomar_sol()

    elif isinstance(animal, Pez):
        animal.nadar()
        animal.formar_banco()
        animal.respirar_brangias()

    elif isinstance(animal, Escarabajo):
        animal.volar()
        animal.excavar()
        animal.rodar_bolas()

    elif isinstance(animal, Pato):
        animal.graznar()
        animal.volar_corto()
        animal.nadar_con_patas()

def crear_animal(tipo):
    if tipo == "caballo":
        return Caballo()
    if tipo == "cocodrilo":
        return Cocodrilo()
    if tipo == "pez":
        return Pez()
    if tipo == "escarabajo":
        return Escarabajo()
    if tipo == "pato":
        return Pato()
    return None

def main():
    bd = BaseDatosAnimales()

    while True:
        menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            tipo = input("Ingrese el tipo de animal: ").lower()
            animal = crear_animal(tipo)
            if animal:
                bd.agregar_final_lista(animal)
            else:
                print("Tipo inválido.")

        elif opcion == "2":
            try:
                pos = int(input("Posición (1-based): ")) - 1
            except ValueError:
                print("Posición inválida.")
                continue
            tipo = input("Tipo de animal: ").lower()
            animal = crear_animal(tipo)
            if animal:
                bd.insertar_elemento_posicion(pos, animal)

        elif opcion == "3":
            bd.eliminar_primer_elemento()

        elif opcion == "4":
            try:
                pos = int(input("Posición a eliminar (1-based): ")) - 1
            except ValueError:
                print("Posición inválida.")
                continue
            bd.eliminar_elemento_posicion(pos)

        elif opcion == "5":
            nombre = input("Nombre del animal: ")
            bd.buscar_por_nombre(nombre)

        elif opcion == "6":
            nombre = input("Nombre del animal: ")
            bd.contar_animales(nombre)

        elif opcion == "7":
            bd.ordenar_por_nombre()

        elif opcion == "8":
            bd.invertir_orden()

        elif opcion == "9":
            bd.imprimir_info()

        elif opcion == "10":
            bd.imprimir_info()
            try:
                pos = int(input("Posición del animal: ")) - 1
            except ValueError:
                print("Posición inválida.")
                continue

            if 0 <= pos < len(bd.lista_animales):
                mostrar_metodos_animal(bd.lista_animales[pos])

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
