from vehiculo import Vehiculo

class Carro(Vehiculo):

    def __init__(self, modelo: str, color: str, motor: str, puertas: int, combustible: str,
                 tipo_luces: str, climatizacion: str):
        super().__init__(modelo, color, motor, puertas, combustible, tipo_luces)
        # ---- Aqui esta el encapsulamiento 
        self.__climatizacion = climatizacion

    def get_climatizacion(self) -> str:
        return self.__climatizacion

    # Creacion de métodos
    def climatizar(self, temperatura: int) -> str:
        return f"El aire del {self.get_modelo()} se pone a {temperatura} grados"

    # El polimorfismo
    def descripcion(self) -> str:
        info_padre = super().descripcion()
        return f"{info_padre} Tiene climatización {self.__climatizacion.lower()}."