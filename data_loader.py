import csv
import processor


def extrac_data(archive):
    data = []

    if not processor.verify_csv_extension(archive):
        return data

    try:
        with open(archive, "r", encoding="utf-8", newline="") as file:
            lector = csv.DictReader(file)

            for linea in lector:
                try:
                    linea["edad"] = int(linea["edad"])
                except (ValueError, TypeError):
                    print("Edad no válida")
                    continue

                try:
                    linea["promedio"] = float(linea["promedio"])
                except (ValueError, TypeError):
                    print("Promedio no válido")
                    continue

                check1 = processor.evaluate_age(linea["edad"])
                check2 = processor.evaluate_average(linea["promedio"])
                check3 = processor.evaluate_name(linea["nombre"])

                if check1 and check2 and check3:
                    data.append(linea)

    except FileNotFoundError:
        print("El archivo no fue encontrado")

    return data


def show_data(data):
    if not data:
        print("No hay datos para mostrar")
        return

    for key in data[0].keys():
        print(f"{key.upper():<13}", end="")
    print()

    for row in data:
        for value in row.values():
            print(f"{value:<13}", end="")
        print()