# se crea la clase padre
class Animal:

    # Constructor y atributos
    def __init__(self, nombre: str, habitat: str, dieta: str, color: str,
                 tamano_adulto: str, vida_maxima: int, desplazamiento: str):
        self.__nombre = nombre
        self.__habitat = habitat
        self.__dieta = dieta
        self.__color = color
        self.__tamano_adulto = tamano_adulto
        self.__vida_maxima = vida_maxima
        self.__desplazamiento = desplazamiento

    def get_nombre(self) -> str:
        return self.__nombre

    def get_habitat(self) -> str:
        return self.__habitat

    def get_dieta(self) -> str:
        return self.__dieta

    def get_color(self) -> str:
        return self.__color

    def get_tamano_adulto(self) -> str:
        return self.__tamano_adulto

    def get_vida_maxima(self) -> int:
        return self.__vida_maxima

    def get_desplazamiento(self) -> str:
        return self.__desplazamiento

    # Creacion de metodos
    def alimentarse(self) -> str:
        return f"El {self.__nombre.lower()} come {self.__dieta}"

    def moverse(self) -> str:
        return f"El {self.__nombre.lower()} se desplaza {self.__desplazamiento}"

    def vida_y_tamano(self) -> str:
        return f"El {self.__nombre.lower()} puede vivir hasta {self.__vida_maxima} años y de adulto mide {self.__tamano_adulto}"

    def descripcion(self) -> str:
        return f"El {self.__nombre.lower()} vive en {self.__habitat}."