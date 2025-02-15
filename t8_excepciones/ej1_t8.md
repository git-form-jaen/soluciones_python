# ¿Cuál es el propósito de la declaración ‘raise’?

La palabra clave ‘raise’ en Python se utiliza para provocar la generación explícita de una excepción. Puede ser utilizada en diferentes contextos para señalar que ha ocurrido una situación excepcional específica y que es necesario interrumpir el flujo normal del programa.


# ¿Cómo puedes crear y usar una excepción personalizada?

Puedes crear una excepción personalizada definiendo una nueva clase que hereda de la clase Exception o de una de sus subclases.

Ejemplo:

```python
class ErrorPersonalizado(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
try:
    raise ErrorPersonalizado("Esto es una excepción personalizada.")
except ErrorPersonalizado as e:
    print(f"Se capturó una excepción: {e}")
```

# Explica para que se usa la declaración ‘assert’

‘Assert’ en Python se utiliza para realizar afirmaciones o verificaciones condicionales en el código. 
 - Si la expresión después de assert evalúa como True, el programa continúa su ejecución normal. 
 - Si la expresión es False, se levanta una excepción AssertionError, interrumpiendo el flujo del programa y proporcionando un mensaje opcional para indicar la causa del fallo.





