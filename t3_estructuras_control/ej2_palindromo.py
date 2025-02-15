# Paso 1: Inicializa una Lista
palabras = ["Ana", "12321", "Una manzana", "radar", "No es palíndromo"]

# Paso 2: Normaliza las Palabras
# Convierte todas las palabras a minúsculas y elimina espacios en blanco alrededor
palabras_normalizadas = [
    palabra.lower().strip() for palabra in palabras if palabra.isalpha()
]

# Paso 3: Identifica los Palíndromos
# Filtra las palabras que son iguales a su reverso
palindromos = [palabra for palabra in palabras_normalizadas if palabra == palabra[::-1]]

# Paso 4: Muestra los Palíndromos
print(palindromos)