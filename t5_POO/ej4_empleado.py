from dataclasses import dataclass


@dataclass
class Empleado:
    nombre: str
    edad: int
    ciudad: str
    empresa: str = "NTER Solutions"  # Variable de clase con valor por defecto

    @staticmethod
    def calcular_salario(base, horas_extras, coste_hora_extra):
        """
        Método estático para calcular el salario de un empleado.

        Args:
            base (float): Salario base del empleado.
            horas_extras (int): Número de horas extras trabajadas.
            coste_hora_extra (float): coste por hora extra.

        Returns:
            float: Salario total.
        """
        return base + (horas_extras * coste_hora_extra)

    @classmethod
    def obtener_nombre_empresa(cls):
        """
        Método de clase para obtener el nombre de la empresa.

        Returns:
            str: Nombre de la empresa.
        """
        return cls.empresa


if __name__ == "__main__":
    # Uso del método de clase
    nombre_empresa = Empleado.obtener_nombre_empresa()
    print(nombre_empresa)  # Salida esperada: NTER Solutions

    # Uso del método estático
    salario = Empleado.calcular_salario(1500, 10, 20)
    print(salario)  # Salida esperada: 1700

    # Creación de una instancia de la clase
    empleado = Empleado(nombre="Carlos", edad=40, ciudad="Barcelona")
    print(
        empleado
    )  # Salida esperada: Empleado(nombre='Carlos', edad=40, ciudad='Barcelona', empresa='NTER Solutions')
