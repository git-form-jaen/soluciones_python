def revertir_palabras(s: str) -> str:
    """
    Invierte el orden de las palabras en una cadena dada, eliminando espacios adicionales.

    Args:
        s (str): La cadena de entrada.

    Returns:
        str: La cadena con el orden de las palabras invertido.
    """
    # Usando lambda para eliminar espacios vacíos y revertir la lista de palabras
    palabras_filtradas = filter(lambda x: x != "", s.split(" "))
    palabras_invertidas = reversed(list(palabras_filtradas))
    return " ".join(palabras_invertidas)


cadenas = ["el cielo es azul", "  hola mundo  ", "un buen   ejemplo"]

for cadena in cadenas:
    print(f"Entrada: '{cadena}' -> Salida: '{revertir_palabras(cadena)}'")