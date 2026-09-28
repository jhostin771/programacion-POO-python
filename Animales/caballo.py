from animal import Animal

class Caballo(Animal):

    def __init__(self, nombre: str, habitat: str, dieta: str, color: str,
                 tamano_adulto: str, vida_maxima: int, desplazamiento: str,
                 raza: str):
        super().__init__(nombre, habitat, dieta, color, tamano_adulto, vida_maxima, desplazamiento)
        # encapsulamiento 
        self.__raza = raza

    def get_raza(self) -> str:
        return self.__raza

    # Creacion de metodos
    def relinchar(self) -> str:
        return f"El {self.get_nombre()} relincha: ¡iiiiii!" # o como aga un caballo

    # polimorfismo
    def descripcion(self) -> str:
        info_padre = super().descripcion()
        return f"{info_padre} Su raza es {self.__raza}."