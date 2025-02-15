# Paso 1: Inicializa una Lista:
nums = [1, 5, 5, 2, 1]

# Paso 2: Elimina Duplicados y Ordena la Lista
nums = sorted(set(nums))

# Paso 3: Muestra el Resultado
print(f"Número de elementos no duplicados: {len(nums)} -> {nums}")

# Paso 4: Define la lista nums2
nums2 = [1, 1, 2]

# Paso 5: Encuentra los elementos comunes y los elementos únicos
set_nums = set(nums)
set_nums2 = set(nums2)

# Elementos comunes en ambas listas
elementos_comunes = set_nums & set_nums2

# Elementos de la primera lista que no están en la segunda
elementos_unicos = set_nums - set_nums2

# Muestra los resultados
print(f"Elementos comunes: {elementos_comunes}")
print(f"Elementos únicos en la primera lista: {elementos_unicos}")