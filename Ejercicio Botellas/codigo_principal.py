
from modelo_botella_plastico import BotellaPlastica
from modelo_botella_vidrio import BotellaVidrio
from modelo_base_datos import BaseDatos

def menu():
    print("\n===== MENÚ DE BOTELLAS =====")
    print("1. Agregar botella al final de la lista (append)")
    print("2. Agregar elementos de otra lista al final (extend)")
    print("3. Insertar botella en posición específica (insert)")
    print("4. Eliminar el primer elemento (pop / remove)")
    print("5. Eliminar elemento por posición (pop)")
    print("6. Buscar botella por material (index / filter)")
    print("7. Contar número de botellas por material (count)")
    print("8. Ordenar elementos de la lista (sort)")
    print("9. Invertir el orden de la lista (reverse)")
    print("10. Imprimir información completa")
    print("11. Ver métodos específicos de una botella")
    print("0. Salir")

def mostrar_metodos_botella(botella):
    print(f"\n--- Métodos específicos de Botella {botella.material} ---")
    if isinstance(botella, BotellaPlastica):
        botella.aplastar()
        botella.reutilizar()
        botella.derretir()
    elif isinstance(botella, BotellaVidrio):
        botella.reciclar()
        botella.enfriar()
        botella.romperse()

def crear_lista_botellas():
    lista_temporal = []
    try:
        cantidad = int(input("¿Cuántas botellas desea agregar? "))
    except ValueError:
        print("Número inválido.")
        return lista_temporal

    for i in range(cantidad):
        print(f"\nBotella {i + 1}:")
        print("a) Plástica")
        print("b) Vidrio")
        tipo = input("Seleccione el tipo: ").lower()
        if tipo == "a":
            botella = BotellaPlastica()
        elif tipo == "b":
            botella = BotellaVidrio()
        else:
            print("Tipo no válido, se omite esta botella.")
            continue
        lista_temporal.append(botella)
    return lista_temporal



def main():
    bd = BaseDatos()

    while True:
        menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("\nSeleccione el tipo de botella a agregar:")
            print("a) Plástica")
            print("b) Vidrio")
            tipo = input("Opción: ").lower()
            if tipo == "a":
                botella = BotellaPlastica()
            elif tipo == "b":
                botella = BotellaVidrio()
            else:
                print("Tipo no válido.")
                continue
            bd.agregar_final_lista(botella)

        elif opcion == "2":
            lista_nueva = crear_lista_botellas()
            if lista_nueva:
                bd.lista_botellas.extend(lista_nueva)
                print(f"Se agregaron {len(lista_nueva)} botella(s) al final usando extend().")
            else:
                print("No se agregaron botellas.")

        elif opcion == "3":
            try:
                pos = int(input("Ingrese la posición donde desea insertar la botella (1-based): ")) - 1
            except ValueError:
                print("Posición inválida.")
                continue
            print("\nSeleccione el tipo de botella a insertar:")
            print("a) Plástica")
            print("b) Vidrio")
            tipo = input("Opción: ").lower()
            if tipo == "a":
                botella = BotellaPlastica()
            elif tipo == "b":
                botella = BotellaVidrio()
            else:
                print("Tipo no válido.")
                continue
            bd.insertar_elemento_posicion(pos, botella)

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
            material = input("Ingrese el material a buscar: ")
            bd.devolver_elemento_si_coincide(material)
            for i, b in enumerate(bd.lista_botellas):
                if b.material.lower() == material.lower():
                    print(f"Índice del primer elemento que coincide: {i + 1}")
                    break

        elif opcion == "7":
            material = input("Ingrese el material a contar: ")
            bd.contar_numero_veces(material)

        elif opcion == "8":
            bd.ordenar_elementos_lista()

        elif opcion == "9":
            bd.invertir_orden()

        elif opcion == "10":
            bd.imprimir_info()

        elif opcion == "11":
            if not bd.lista_botellas:
                print("La lista está vacía.")
            else:
                bd.imprimir_info()
                try:
                    pos = int(input("Ingrese la posición de la botella para ver sus métodos específicos (1-based): ")) - 1
                except ValueError:
                    print("Posición inválida.")
                    continue
                if 0 <= pos < len(bd.lista_botellas):
                    mostrar_metodos_botella(bd.lista_botellas[pos])
                else:
                    print("Posición inválida.")

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
