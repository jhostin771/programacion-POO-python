from vehiculo import Vehiculo

class Camion(Vehiculo):

    def __init__(self, modelo: str, color: str, motor: str, puertas: int, combustible: str,
                 tipo_luces: str, capacidad_carga: int, seguridad: str):
        super().__init__(modelo, color, motor, puertas, combustible, tipo_luces)
        # Otro encapsulamiento 
        self.__capacidad_carga = capacidad_carga
        self.__seguridad = seguridad

    def get_capacidad_carga(self) -> int:
        return self.__capacidad_carga

    def get_seguridad(self) -> str:
        return self.__seguridad

    # Creacion de métodos
    def cargar(self, peso: int) -> str:
        if peso <= self.__capacidad_carga:
            return f"El {self.get_modelo()} puede cargar {peso} kg"
        return f"El {self.get_modelo()} solo puede cargar por debajo de {peso} kg"

    def seguridad_info(self) -> str:
        return f"Seguridad del {self.get_modelo()}: {self.__seguridad}"

    # ---- el polimorfismo ----
    def descripcion(self) -> str:
        info_padre = super().descripcion()
        return f"{info_padre} Puede cargar hasta {self.__capacidad_carga} kg."