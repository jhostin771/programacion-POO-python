# Creacion de la clase padre
class Vehiculo:

    # Crear Constructor y atributos
    def __init__(self, modelo: str, color: str, motor: str, puertas: int, combustible: str, tipo_luces: str):
        self.__modelo = modelo
        self.__color = color
        self.__motor = motor
        self.__puertas = puertas
        self.__combustible = combustible
        self.__tipo_luces = tipo_luces

    def get_modelo(self) -> str:
        return self.__modelo

    def get_color(self) -> str:
        return self.__color

    def get_motor(self) -> str:
        return self.__motor

    def get_puertas(self) -> int:
        return self.__puertas

    def get_combustible(self) -> str:
        return self.__combustible

    def get_tipo_luces(self) -> str:
        return self.__tipo_luces

    # Creacion de métodos
    def luces(self) -> str:
        return f"El {self.__modelo} tiene luces {self.__tipo_luces}"

    def descripcion(self) -> str:
        return f"Es un {self.__modelo} de color {self.__color.lower()} y usa {self.__combustible.lower()}."