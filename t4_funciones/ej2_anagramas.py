from collections.abc import Container
from typing import List


def buscar_anagramas(palabra: str, dictionario: Container) -> List[str]:
    """
    Encuentra todos los anagramas de una palabra en un contenedor dado.

    Esta función busca coincidencias de anagramas para una palabra específica,
    donde un anagrama es una reordenación de las letras de la palabra original
    que forma otra palabra contenida en el diccionario proporcionado.

    Args:
        palabra: Cadena de la palabra objetivo.
        dictionario: Un objeto de tipo collections.abc.Container que contiene
                    todas las cadenas que son palabras conocidas.

    Returns:
        List[str]: Lista de anagramas encontrados. Vacía si no se encontró ninguno.
    """

    palabra_ordenada = sorted(palabra)
    return [w for w in dictionario if sorted(w) == palabra_ordenada]


if __name__ == "__main__":
    dictionario = ["enlists", "foo", "bar", "inlets", "listen", "silent"]

    palabra = "listen"
    anagramas = buscar_anagramas(palabra, dictionario)
    print(f"Anagramas encontrados para la palabra '{palabra}': {anagramas}")
