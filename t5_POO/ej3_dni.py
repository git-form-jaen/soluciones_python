class Dni:
    def __init__(self, numero):
        self.numero = numero

    def __calcular_letra(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        return letras[int(self.numero) % 23]

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        if len(numero) == 8 and numero.isdigit():
            self._numero = numero
            self._letra = self.__calcular_letra()
        else:
            self._numero = "incorrecto"
            self._letra = "#"

    def __str__(self):
        return f"DNI: {self.numero}-{self._letra}"


if __name__ == "__main__":
    dni_valido = Dni("12345678")
    print(dni_valido)  # Salida esperada: DNI: 12345678-Z

    dni_invalido = Dni("1234ABC8")
    print(dni_invalido)  # Salida esperada: DNI: 00000000-#