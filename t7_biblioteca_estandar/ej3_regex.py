import os
import re

# Listar todos los archivos en el directorio actual y filtrar aquellos que sean archivos TXT
files = os.listdir(os.getcwd())
txt_files = [file for file in files if file.endswith(".txt")]

# Definir un patrón regex para buscar palabras que terminan en '!'
search_regex = re.compile(
    r"¡?\s?\w*\!"
)  # Coincide con todas las palabras que terminan en '!'

# Abrir cada archivo TXT y buscar el patrón regex
for doc in txt_files:
    with open(doc, "r", encoding="utf-8") as opened_file:
        contents = opened_file.read()
        found = search_regex.findall(contents)
        if found:
            found_str = " ".join(found)
            print(
                f"En el archivo '{doc}', se encontraron las siguientes coincidencias: {found_str}"
            )
        else:
            print(f"En el archivo '{doc}', no se encontraron coincidencias.")
