# Explica las diferencias entre una lista y una tupla en Python:
 1. Mutabilidad:
 - Listas: Son mutables, lo que significa que puedes modificar sus elementos (agregar, eliminar, cambiar).
 - Tuplas: Son inmutables; sus elementos no pueden ser cambiados después de su creación.

 2. Sintaxis:
 - Listas: Usan corchetes [ ... ].
 - Tuplas: Usan paréntesis ( ... ).

 3. Rendimiento:
 - Listas: Generalmente más lentas y requieren más memoria que las tuplas.
 - Tuplas: Generalmente más rápidas y requieren menos memoria que las listas.


# ¿Cómo puedes invertir una lista en Python?

Puedes invertir una lista en Python usando uno de los siguientes métodos:
1. Usando el método reverse():
mi_lista = [1, 2, 3, 4, 5]
mi_lista.reverse()  # Invierte la lista en su lugar.

2. Usando slicing:
mi_lista = [1, 2, 3, 4, 5]
lista_invertida = mi_lista[::-1]  # Crea una nueva lista invertida sin modificar la lista original.



# ¿Cuál es la diferencia entre los métodos append() y extend() para listas?

append(): Se utiliza para agregar un único elemento al final de una lista.

mi_lista = [1, 2, 3]
mi_lista.append(42)
mi_lista ahora es [1, 2, 3, 42]

extend(): Se utiliza para agregar los elementos de un iterable (por ejemplo, otra lista) al final de una lista.
mi_lista = [1, 2, 3]
mi_lista.extend([4, 5, 6])
mi_lista ahora es [1, 2, 3, 4, 5, 6]