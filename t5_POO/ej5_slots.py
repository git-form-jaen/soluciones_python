class Dog:
    __slots__ = ["nombre", "edad"]


dog = Dog()
dog.name = "Bobby"
dog.edad = 3
dog.genero = "m"


"""
Se intenta asignar el valor 'm' al atributo género de la instancia dog. Esto genera un AttributeError porque gender no está definido en __slots__.
__slots__ especifica una lista de atributos permitidos para las instancias de esa clase.
Al definir __slots__, se impide que la instancia tenga un diccionario __dict__; 
se utiliza un modelo de almacenamiento alternativo para los atributos de instancia: los atributos se almacenan en un array, 
que consume significativamente menos memoria que un diccionario.
"""
