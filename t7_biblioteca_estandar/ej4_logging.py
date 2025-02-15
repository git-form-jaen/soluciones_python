import logging

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Configurar el logger
logger = logging.getLogger("t4_logger")
logger.setLevel(logging.DEBUG)

# Crear manejador para WARNING
handler_warning = logging.FileHandler("t4_warning.log")
handler_warning.setLevel(logging.WARNING)
handler_warning.setFormatter(formatter)
logger.addHandler(handler_warning)

# Crear manejador para CRITICAL
handler_critical = logging.FileHandler("t4_critical.log")
handler_critical.setLevel(logging.CRITICAL)
handler_critical.setFormatter(formatter)
logger.addHandler(handler_critical)


# Función para generar mensajes de registro en todos los niveles
def logging_messages():
    logger.debug("Este es un mensaje DEBUG")
    logger.info("Este es un mensaje INFO")
    logger.warning("Este es un mensaje WARNING")
    logger.error("Este es un mensaje ERROR")
    logger.critical("Este es un mensaje CRITICAL")


# Función para verificar el contenido de los archivos de registro
def check_log_content(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


if __name__ == "__main__":
    logging_messages()
    # Verificar el contenido del archivo t4_warning.log
    warning_log_records = check_log_content("t4_warning.log")
    print("Contenido de t4_warning.log:")
    for record in warning_log_records:
        print(record.strip())

    # Verificar el contenido del archivo t4_critical.log
    critical_log_records = check_log_content("t4_critical.log")
    print("\nContenido de t4_critical.log:")
    for record in critical_log_records:
        print(record.strip())
