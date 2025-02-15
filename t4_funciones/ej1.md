# ¿Qué es un decorador y cómo se utiliza?

Un decorador en Python es una función envolvente que puede modificar o mejorar el comportamiento de otra función o método. Los decoradores son funciones exteriores que envuelven funciones interiores. A menudo se utilizan para agregar funcionalidad a las funciones, como el registro de logs. Se aplican utilizando el símbolo ‘@’ seguido del nombre del decorador encima de la definición de una función.

@mi_decorador
def mi_funcion():
    Código de la función aquí

# ¿Qué es una función lambda?

Una función lambda, también conocida como función anónima, es una pequeña función sin nombre definida utilizando la palabra clave ‘lambda’. Las funciones lambda se utilizan a menudo para operaciones cortas y simples que pueden definirse en una sola línea de código. Son particularmente útiles como argumentos para funciones de orden superior como map(), filter() y sorted().


# ¿Qué es un docstring?

Un docstring en Python es un literal de cadena utilizado para proporcionar documentación o información descriptiva sobre un módulo, función, clase o método. Se encierra dentro de comillas triples (''' o """) y se coloca inmediatamente debajo de la definición de la entidad de Python que describe. Los docstrings son accesibles a través del atributo .__doc__ y se utilizan comúnmente para proporcionar información sobre el propósito, uso y parámetros de las funciones y clases.


def mi_funcion():
    """Esta es una docstring que describe la función."""
    pass

# Explica el concepto de funciones de primera clase.

Las funciones de primera clase son funciones que pueden ser tratadas como objetos, lo que significa que pueden ser asignadas a variables, pasadas a otras funciones como argumentos y devueltas desde otras funciones.
