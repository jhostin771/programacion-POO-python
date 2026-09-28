from animal import Animal

class Escarabajo(Animal):

    def __init__(self, nombre: str, habitat: str, dieta: str, color: str,
                 tamano_adulto: str, vida_maxima: int, desplazamiento: str,
                 tiene_cuerno: bool):
        super().__init__(nombre, habitat, dieta, color, tamano_adulto, vida_maxima, desplazamiento)
        # Otro encapsulamiento
        self.__tiene_cuerno = tiene_cuerno

    def get_tiene_cuerno(self) -> bool:
        return self.__tiene_cuerno

    # Creacion de metodos
    def pelear(self) -> str:
        if self.__tiene_cuerno:
            return f"El {self.get_nombre()} usa su cuerno para pelear"
        return f"El {self.get_nombre()} no sirve para pelear"

    # polimorfismo
    def descripcion(self) -> str:
        info_padre = super().descripcion()
        if self.__tiene_cuerno:
            return f"{info_padre} Tiene un cuerno."
        return f"{info_padre} No tiene cuerno."