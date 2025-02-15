# ¿Cuál es el propósito de la declaración if __name__ == "__main__":?

La declaración if __name__ == "__main__": se usa para verificar si un script de Python se está ejecutando como el programa principal o si se está importando como un módulo en otro script. Proporciona una manera de separar el código ejecutable de los módulos reutilizables. El código dentro de este bloque solo se ejecutará si el script se ejecuta directamente, no cuando se importe como un módulo en otro script. Esto se usa comúnmente para crear módulos reutilizables en Python.

# ¿Para qué sirve la función super() en Python?

La función super() se utiliza para llamar a un método de una clase padre dentro de una clase hija. Se usa a menudo en el método __init__ de una clase hija para invocar el constructor de la clase padre. Esto permite inicializar atributos y comportamientos de la clase padre mientras se añaden o sobrescriben funcionalidades en la clase hija.

# Describe el uso del decorador @staticmethod

El decorador @staticmethod se usa para definir un método estático dentro de una clase. Los métodos estáticos están asociados con la clase en lugar de con las instancias de la clase. No requieren acceso a datos específicos de la instancia y se pueden llamar en la propia clase sin crear una instancia.

