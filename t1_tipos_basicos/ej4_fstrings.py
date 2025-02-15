# 1. Incorporar variables en un string
nombre = "Miguel"
edad = 30
# Usamos f-strings para incluir las variables nombre y edad en una cadena de texto.
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

# 2. Realizar operaciones aritméticas
a = 5
b = 10
# Usamos f-strings para realizar la operación aritmética a + b y mostrar el resultado en una cadena de texto.
print(f"Cinco más diez es {a + b}.")

# 3. Formatear números
pi = 3.14159265
# Usamos f-strings para formatear el número pi y mostrarlo redondeado a dos decimales.
print(f"El valor de pi redondeado a dos decimales es {pi:.2f}.")

# 4. Incluir expresiones condicionales
score = 65
# Usamos f-strings para incluir una expresión condicional que determine si la calificación es "aprobado" o "suspendido".
print(f"Tu calificación es {'aprobado' if score >= 50 else 'suspendido'}.")

# 5. Ejemplo de depuración con f-strings
base = 10
altura = 5

# Verificando los valores de las variables antes de calcular el área
# Usamos f-strings para imprimir las variables base y altura con sus nombres, útil para la depuración.
print(f"{base=}")  # Imprimirá base=10
print(f"{altura=}")  # Imprimirá altura=5

area = base * altura
# Usamos f-strings para imprimir la variable area con su nombre, útil para la depuración.
print(f"{area=}")  # Imprimirá area=50