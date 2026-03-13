import data_loader
import utils
import exporter

def CLI_window(data):
    while(True):
        print("Seleccione una de las siguientes opciones:")
        print("1) Cargar datos") #check
        print("2) Filtrar") #check
        print("3) Ordenar") #check
        print("4) Mostrar estadísticas") #check
        print("5) Exportar resultados") #check
        print("6) Salir") #check

        option = input(">> ").strip()

        match option:
            case '1':
                option1(data)

            case '2':
                option2(data)

            case '3':
                option3(data)

            case '4':
                option4(data)

            case '5':
                option5(data)

            case '6':
                print("Saliendo de la consola ....")
                break

            case _:
                print("Opción no validad. Intente nuevamente.\n")


# ==========================================
#             O P C I Ó N    1
# ==========================================
def option1(data):
    print("\n=======================================================")
    data_loader.show_data(data)
    print("=======================================================\n")


# ==========================================
#             O P C I Ó N    2
# ==========================================
def option2(data):
    while(True):
        print("\nElija una de las opciones de filtrado:")
        print("\t1) Filtrar por promedio mayor a X")
        print("\t2) Filtrar por carrera")
        print("\t3) Filtrar por edad mínima")
        print("\t4) Volver")

        option = input(">> ").strip()

        match option:
            case '1':
                average = float(input("Ingrese el valor mínimo de promedio: "))
                data_filter = utils.filter_average(data, average)
                option1(data_filter)
                break

            case '2':
                career = input("Ingrese el nombre de la carrera: ").strip()
                data_filter = utils.filter_career(data, career)
                option1(data_filter)
                break

            case '3':
                age = int(input("Ingrese la edad mínima: "))
                data_filter = utils.filter_age(data, age)
                option1(data_filter)
                break

            case '4':
                print("Volviendo al tablero...\n")
                break

            case _:
                print("Opción no validad. Intente nuevamente.\n")


# ==========================================
#             O P C I Ó N    3
# ==========================================
def option3(data):
    while(True):
        print("Elija una de las opciones para ordenamiento:")
        print("\t1) Ordenar por nombre")
        print("\t2) Ordenar por promedio")
        print("\t3) Ordenar por edad")
        print("\t4) Volver")

        option = input(">> ")

        match option:
            case '1':
                data_sorted = utils.sorted_data(data, "nombre")
                option1(data_sorted)
                break

            case '2':
                data_sorted = utils.sorted_data(data, "promedio")
                option1(data_sorted)
                break

            case '3':
                data_sorted = utils.sorted_data(data, "edad")
                option1(data_sorted)
                break

            case '4':
                print("Volviendo al tablero...\n")
                break

            case _:
                print("Opción no validad. Intente nuevamente.\n")



# ==========================================
#             O P C I Ó N    4
# ==========================================
def option4(data):
    print("----------------------------------------------")
    print("           E S T A D Í S T I C A              ")
    print("----------------------------------------------")
    mean = utils.mean_calculation(data, "promedio")
    print(f"Promedio general: {mean}")

    min_age = utils.min_age(data)
    print(f"Edad mínima: {min_age}")

    max_age = utils.max_age(data)
    print(f"Edad máxima: {max_age}")

    print("Conteo por carrera:")
    career_counter = utils.count_career(data)
    for key, value in career_counter.items():
        print(f"\t{key}: {value}")
    print()


# ==========================================
#             O P C I Ó N    5
# ==========================================
def option5(data):
    file_export = {
        "promedio general": utils.mean_calculation(data,"promedio"),
        "total de estudiante": len(data),
        "edad maxima": utils.max_age(data),
        "edad minima": utils.min_age(data),
        "cantidad por carrera" : utils.count_career(data)
    }
    exporter.export_JSON(file_export)
    print("Los resultados han sido exportados")
