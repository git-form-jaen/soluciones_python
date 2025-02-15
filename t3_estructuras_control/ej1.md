# ¿Cuál es el propósito de la función enumerate en Python?

La función enumerate en Python es una herramienta muy útil para iterar sobre un iterable mientras se mantiene el seguimiento del índice de cada elemento. Devuelve una tupla con el índice y el elemento, lo que facilita el acceso a ambos en un bucle. Es especialmente útil en situaciones donde necesitas trabajar con ambos valores simultáneamente.

lista = ['a', 'b', 'c', 'd']

for indice, valor in enumerate(lista, start=1):
    print(f"Índice: {indice}, Valor: {valor}")

Salida esperada:

Índice: 1, Valor: a
Índice: 2, Valor: b
Índice: 3, Valor: c
Índice: 4, Valor: d

# Explica el concepto de comprensiones de listas.

Las comprensiones de listas son una manera concisa y legible de crear listas en Python. Permiten generar una nueva lista aplicando una expresión a cada elemento de un iterable existente (como una lista, tupla o rango) y, opcionalmente, aplicar un filtro. La sintaxis básica es [expresión for elemento in iterable if condición]. Las comprensiones de listas son una alternativa más 'pythonica' y eficiente a los bucles for tradicionales para crear listas