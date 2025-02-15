s = '   E.T., teléfono, mi casa  '

# 2. Muestra la longitud de la variable anterior.
# Utilizamos la función len() para obtener la longitud de la cadena.
longitud = len(s)
print("Longitud de la cadena:", longitud)

# 3. Elimina los caracteres de espacio en blanco al comienzo y final del string
s = s.strip()
print("Cadena sin espacios en blanco al final:", s)

# 4. Muestra el primer carácter del string.
primer_caracter = s[0]
print("Primer carácter del string:", primer_caracter)

# 5. Muestra el penúltimo carácter del string.
penultimo_caracter = s[-2]
print("Penúltimo carácter del string:", penultimo_caracter)

# 6. Convierte la cadena a minúsculas.
s = s.lower()
print("Cadena en minúsculas:", s)

# 8. Busca la posición de la subcadena 'mi' en la cadena.
posicion_mi = s.find('mi')
print("Posición de 'mi' en la cadena:", posicion_mi)

# 9. Reemplaza la palabra 'casa' por 'coche'.
s2 = s.replace('casa', 'coche')
print("Cadena con 'casa' reemplazada por 'coche':", s2)

# 7. Divide la cadena en una lista de subcadenas utilizando la coma como delimitador
s2_split = s2.split(',')
print("Cadena dividida en subcadenas:", s2_split)