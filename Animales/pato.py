from animal import Animal

class Pato(Animal):

    def __init__(self, nombre: str, habitat: str, dieta: str, color: str,
                 tamano_adulto: str, vida_maxima: int, desplazamiento: str,
                 huevos: int):
        super().__init__(nombre, habitat, dieta, color, tamano_adulto, vida_maxima, desplazamiento)
        # Otro encapsulamiento 
        self.__huevos = huevos

    def get_huevos(self) -> int:
        return self.__huevos

    # Creacion de metodos
    def graznar(self) -> str:
        return f"El {self.get_nombre()} hace: ¡cuac cuac! 🦆"

    # polimorfismo
    def descripcion(self) -> str:
        info_padre = super().descripcion()
        return f"{info_padre} Pone {self.__huevos} huevos por nido."