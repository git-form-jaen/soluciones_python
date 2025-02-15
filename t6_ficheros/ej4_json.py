import json


def escribir_fichero(inventario):
    """
    Escribe el inventario en un archivo JSON.

    Args:
        inventario (list): La lista de productos en el inventario.
    """
    with open("inventario.json", "w", encoding="utf-8") as file:
        json.dump(inventario, file, indent=4)
        print("Inventario guardado en inventario.json")


def agregar_producto(inventario, producto):
    """
    Agrega un producto al inventario

    Args:
        inventario (list): La lista de productos en el inventario.
        producto (dict): El diccionario con los detalles del producto a agregar.
    """
    inventario.append(producto)
    print(f"Producto agregado: {producto['nombre']}")


if __name__ == "__main__":
    # Cargar los datos de los productos existentes en el inventario
    with open("files/productos.json", "r", encoding="utf-8") as archivo_json:
        inventario = json.load(archivo_json)
        print("Inventario cargado de productos.json")

    # Ejemplo de uso: Agregar un nuevo producto
    nuevo_producto = {"nombre": "Laptop", "cantidad": 10, "precio": 999.99}
    agregar_producto(inventario, nuevo_producto)
    escribir_fichero(inventario)