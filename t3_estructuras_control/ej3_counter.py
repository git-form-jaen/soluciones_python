from collections import Counter
from collections import defaultdict

# Paso 1: Inicialización de la Palabra
palabra_ejemplo = "marsupilami"

# Paso 2: Usando un Diccionario Normal
contador1 = {}
for letra in palabra_ejemplo:
    if letra not in contador1:
        contador1[letra] = 1
    else:
        contador1[letra] += 1

print("Frecuencias usando un diccionario:")
for letra, frecuencia in sorted(contador1.items()):
    print(f"Letra '{letra}': {frecuencia}")

# Paso 3: Usando Defaultdict

contador2 = defaultdict(int)
for letra in palabra_ejemplo:
    contador2[letra] += 1

print("\nFrecuencias usando defaultdict:")
for letra, frecuencia in sorted(contador2.items()):
    print(f"Letra '{letra}': {frecuencia}")

# Paso 4: Usando Counter de Collections

contador_palabras2 = Counter(palabra_ejemplo)

print("\nFrecuencias usando Counter:")
for letra, frecuencia in sorted(contador_palabras2.items()):
    print(f"Letra '{letra}': {frecuencia}")



