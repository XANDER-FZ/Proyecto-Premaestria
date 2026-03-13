def verify_csv_extension(file_path):
    try:
        if file_path is None:
            raise FileNotFoundError("No se recibió ninguna ruta de archivo")

        if not isinstance(file_path, str):
            raise TypeError("La ruta del archivo debe ser un string")

        if file_path.strip() == "":
            raise FileNotFoundError("La ruta del archivo está vacía")

        if not file_path.lower().endswith(".csv"):
            raise ValueError("El archivo debe tener extensión .csv")

        return True

    except (ValueError, FileNotFoundError, TypeError) as e:
        print(f"Error: {e}")
        return False


def evaluate_age(age):
    try:
        if age is None:
            raise ValueError("La edad no puede ser None")

        if not isinstance(age, int):
            raise TypeError("La edad debe ser un entero")

        if age <= 0:
            raise ValueError("La edad debe ser un número positivo")

        return True

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return False


def evaluate_average(average):
    try:
        if average is None:
            raise ValueError("El promedio no puede ser None")

        if not isinstance(average, (int, float)):
            raise TypeError("El promedio debe ser numérico")

        if average < 0 or average > 10:
            raise ValueError("El promedio debe estar entre 0 y 10")

        return True

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return False


def evaluate_name(name):
    try:
        if name is None:
            raise ValueError("El nombre no puede ser None")

        if not isinstance(name, str):
            raise TypeError("El nombre debe ser un string")

        if name.strip() == "":
            raise ValueError("El nombre no puede estar en blanco")

        return True

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return False
