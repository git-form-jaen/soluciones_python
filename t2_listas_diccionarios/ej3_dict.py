# Definiendo el diccionario usando dict()
vehiculos_dict = dict(coche=10, motocicleta=20, camión=30)
print("Usando dict():", vehiculos_dict)

# Definiendo el diccionario usando {}
vehiculos = {"coche": 10, "motocicleta": 20, "camión": 30}
print("Usando {}:", vehiculos)

# Definiendo el diccionario usando zip()
claves = ["coche", "motocicleta", "camión"]
valores = [10, 20, 30]
vehiculos_zip = dict(zip(claves, valores))
print("Usando zip():", vehiculos_zip)

# Mostrando los valores del diccionario
print("Valores:", vehiculos.values())

# Mostrando las claves del diccionario
print("Claves:", vehiculos.keys())

# Mostrando el valor de "coche"
print("Valor de coche:", vehiculos["coche"])

# Añadiendo "avión" con valor 100
vehiculos["avión"] = 100
print("Añadiendo avión:", vehiculos)

# Mostrando los elementos del diccionario
print("Elementos del diccionario:", vehiculos.items())