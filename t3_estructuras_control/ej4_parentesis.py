from collections import deque

s = "{[()()]()}"
# s = "{[()()]()]}"


brackets = {"(": ")", "{": "}", "[": "]"}

# Usando deque como una pila
pila = deque()

for bracket in s:
    if bracket in brackets:
        pila.append(bracket)
    elif not pila or brackets[pila.pop()] != bracket:
        print("La cadena de paréntesis es inválida.")
        break
else:
    if not pila:
        print("La cadena de paréntesis es válida.")
    else:
        print("La cadena de paréntesis es inválida.")