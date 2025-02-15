# Parte 1: Números Complejos

# 1. Define dos números de tipo complejo.
d = 3 + 4j
e = 1 - 2j

# 2. Muestra por pantalla la parte real del primer número definido en el punto 1.
# Usamos el atributo .real para obtener la parte real del número complejo.
print(f"La parte real del primer número es: {d.real}")

# 3. Muestra por pantalla la parte imaginaria del segundo número definido en el punto 1.
# Usamos el atributo .imag para obtener la parte imaginaria del número complejo.
print(f"La parte imaginaria del segundo número es: {e.imag}")

# 4. Define la variable f con el resultado de la multiplicación de los dos números complejos
f = d * e
# Muestra el resultado de la multiplicación.
print(f"El resultado de la multiplicación de d y e es: {f}")

# Parte 2: Operadores Bit a Bit

# 5. Define una variable num con un número entero.
num = 42  

# 6. Utiliza el operador bit a bit AND (&) para verificar si el número es par.
# La operación num & 1 verifica el bit menos significativo del número.
# Si el resultado es 0, el número es par; si es 1, el número es impar.
es_par = (num & 1) == 0

# 7. Muestra por pantalla un mensaje indicando si el número es par o impar utilizando f-strings
print(f"El número {num} es {'par' if es_par else 'impar'}.")