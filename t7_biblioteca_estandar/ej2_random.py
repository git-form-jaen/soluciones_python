import random
import itertools

# Lista inicial de frutas
frutas = ["manzana", "plátano", "cereza", "mango", "piña", "fresa"]

# Seleccionar una fruta aleatoria para la base del batido
base_batido = random.choice(frutas)
print(f"La fruta base para el batido es: {base_batido}")

# Mezclar las frutas y seleccionar las dos primeras para añadir al batido
random.shuffle(frutas)
frutas_para_agregar = frutas[:2]
print(f"Frutas adicionales para el batido: {frutas_para_agregar}")

# 3. Elegir una muestra de tres frutas para decorar el batido
frutas_decorativas = random.sample(frutas, 3)
print(f"Frutas para decorar el batido: {frutas_decorativas}")

# 4. Usamos itertools para generar todas las combinaciones posibles de tres frutas
combinaciones = list(itertools.combinations(frutas, 3))
print("Todas las combinaciones posibles de tres frutas son:")
for combinacion in combinaciones:
    print(combinacion)
