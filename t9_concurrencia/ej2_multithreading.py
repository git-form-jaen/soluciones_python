import threading


def leer_archivo(ruta_archivo):
    with open(ruta_archivo, "r") as archivo:
        contenido = archivo.read()
    return contenido


def lector_archivos_multihilo(rutas_archivos):
    hilos = []
    resultados = {}

    def leer_archivo_hilo(ruta_archivo):
        resultado = leer_archivo(ruta_archivo)
        resultados[ruta_archivo] = resultado

    # Crear e iniciar hilos
    for ruta_archivo in rutas_archivos:
        hilo = threading.Thread(target=leer_archivo_hilo, args=(ruta_archivo,))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    return resultados


if __name__ == "__main__":
    rutas_archivos = ["archivo1.txt", "archivo2.txt", "archivo3.txt", "archivo4.txt"]
    resultados_multihilo = lector_archivos_multihilo(rutas_archivos)
