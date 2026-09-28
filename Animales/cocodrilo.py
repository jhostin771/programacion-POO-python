from animal import Animal

class Cocodrilo(Animal):

    def __init__(self, nombre: str, habitat: str, dieta: str, color: str,
                 tamano_adulto: str, vida_maxima: int, desplazamiento: str,
                 dientes: int):
        super().__init__(nombre, habitat, dieta, color, tamano_adulto, vida_maxima, desplazamiento)
        # Otro encapsulamiento 
        self.__dientes = dientes

    def get_dientes(self) -> int:
        return self.__dientes

    # Creacion de métodos
    def morder(self) -> str:
        return f"El {self.get_nombre()} cierra su boca y muerde a su presa"

    # polimorfismo
    def descripcion(self) -> str:
        info_padre = super().descripcion()
        return f"{info_padre} Tiene {self.__dientes} dientes."