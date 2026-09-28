from vehiculo import Vehiculo

class Van(Vehiculo):

    def __init__(self, modelo: str, color: str, motor: str, puertas: int, combustible: str,
                 tipo_luces: str, capacidad_pasajeros: int):
        super().__init__(modelo, color, motor, puertas, combustible, tipo_luces)
        #  Otro encapsulamiento 
        self.__capacidad_pasajeros = capacidad_pasajeros

    def get_capacidad_pasajeros(self) -> int:
        return self.__capacidad_pasajeros

    # Creacion de métodos
    def pasajeros_info(self, pasajeros: int) -> str:
        if pasajeros <= self.__capacidad_pasajeros:
            return f"Sí caben {pasajeros} pasajeros"
        return f"No caben {pasajeros} pasajeros, solo caben {self.__capacidad_pasajeros}"

    def espejos(self, accion: str) -> str:
        return f"{accion} los espejos del {self.get_modelo()}"

    # Un polimorfismo
    def descripcion(self) -> str:
        info_padre = super().descripcion()
        return f"{info_padre} Tiene espacio para {self.__capacidad_pasajeros} pasajeros."