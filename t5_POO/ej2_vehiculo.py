class Vehicle:
    owner = "NWorld"  # Variable de clase

    def __init__(self, nombre, velocidad_maxima, kilometraje):
        self.nombre = nombre
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

    def mostrar_capacidad(self, capacidad):
        """
        Imprime la capacidad del vehículo.

        Args:
            capacidad (int): La capacidad del vehículo.
        """
        print(f"La capacidad de {self.nombre} es de {capacidad}.")


class Bus(Vehicle):
    def mostrar_capacidad(self, capacidad=50):
        """
        Imprime la capacidad del bus, con una capacidad por defecto de 50.

        Args:
            capacidad (int, optional): La capacidad del bus. Default es 50.
        """
        print(f"La capacidad de {self.nombre} es de {capacidad}.")


# Crear una instancia de la clase Vehicle
vehiculo = Vehicle("Coche", 180, 15000)
vehiculo.mostrar_capacidad(5)  # Salida esperada: La capacidad de Coche es de 5.

# Crear una instancia de la clase Bus
bus = Bus("Autobús Escolar", 120, 30000)
bus.mostrar_capacidad()  # Salida esperada: La capacidad de Autobús Escolar es de 50.
bus.mostrar_capacidad(75)  # Salida esperada: La capacidad de Autobús Escolar es de 75.

# Verificar la variable owner
print(Vehicle.owner)  # Salida esperada: NWorld
print(Bus.owner)  # Salida esperada: NWorld
print(vehiculo.owner)  # Salida esperada: NWorld
print(bus.owner)  # Salida esperada: NWorld
