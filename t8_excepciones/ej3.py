import logging

# Configurar logging
logging.basicConfig(
    filename="data_analysis.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class InvalidDataError(Exception):
    def __init__(self, message):
        super().__init__(message)


def leer_datos(file_path):
    try:
        with open(file_path, "r") as file:
            datos = file.read().splitlines()
            # Convertir los datos a enteros o flotantes
            return [float(dato) for dato in datos]
    except FileNotFoundError:
        logging.error("El archivo no se encontró.")
        raise
    except ValueError as e:
        logging.error(f"Error al convertir datos: {e}")
        raise InvalidDataError("El archivo contiene datos no numéricos.")
    except Exception as e:
        logging.error(f"Ocurrió un error inesperado: {e}")
        raise


def validar_datos(datos):
    if not all(isinstance(i, (int, float)) for i in datos):
        raise InvalidDataError("Todos los elementos deben ser números.")
    if len(datos) == 0:
        raise InvalidDataError("La lista de datos no puede estar vacía.")


def analizar_datos(datos):
    try:
        # Validar los datos
        validar_datos(datos)

        # Calcular la media de los datos
        media = sum(datos) / len(datos)
        logging.info(f"La media de los datos es: {media}")
        print(f"La media de los datos es: {media}")

        print(datos[2])  # Acceso válido
        print(datos[3] * datos)  # Acceso fuera de rango y operación con listas

    except InvalidDataError as e:
        logging.error(f"Error de datos inválidos: {e}")
        print(f"Error de datos inválidos: {e}")

    except IndexError:
        logging.error("Índice fuera de rango.")
        print("Índice fuera de rango.")

    except TypeError as e:
        logging.error(f"Error de tipo: {e}")
        print(f"Error de tipo: {e}")

    except Exception as e:
        logging.error(f"Ocurrió otra excepción: {e}")
        print(f"Ocurrió otra excepción: {e}")

    else:
        logging.info("Los datos se procesaron y manipularon correctamente.")
        print("Los datos se procesaron y manipularon correctamente.")

    finally:
        logging.info("Fin del proceso de validación, análisis y manipulación de datos.")
        print("Fin del proceso de validación, análisis y manipulación de datos.")


if __name__ == "__main__":
    file_path = "files/ej3_datos.txt"

    try:
        datos = leer_datos(file_path)
        analizar_datos(datos)
    except Exception as e:
        print(f"Error crítico: {e}")
