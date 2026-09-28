from animal import Animal

class Pez(Animal):

    def __init__(self, nombre: str, habitat: str, dieta: str, color: str,
                 tamano_adulto: str, vida_maxima: int, desplazamiento: str,
                 tipo_agua: str):
        super().__init__(nombre, habitat, dieta, color, tamano_adulto, vida_maxima, desplazamiento)
        # Otro encapsulamiento 
        self.__tipo_agua = tipo_agua

    def get_tipo_agua(self) -> str:
        return self.__tipo_agua

    # Creacion de metodos
    def nadar_en_grupo(self, cantidad: int) -> str:
        return f"El {self.get_nombre()} nada junto a {cantidad} peces más"

    # polimorfismo
    def descripcion(self) -> str:
        info_padre = super().descripcion()
        return f"{info_padre} Es de agua {self.__tipo_agua}."