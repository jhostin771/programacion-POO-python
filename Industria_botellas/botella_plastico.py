from botella import Botella

class BotellaPlastico(Botella):

    def __init__(self, material: str, capacidad: str, forma: str, diseno: str, tapa: str, grabados: bool,
                 flexibilidad: str, temperatura_maxima: int):
        super().__init__(material, capacidad, forma, diseno, tapa, grabados)
        # ---- Otro encapsulamiento ----
        self.__flexibilidad = flexibilidad
        self.__temperatura_maxima = temperatura_maxima

    def get_flexibilidad(self) -> str:
        return self.__flexibilidad

    def compatibilidad_con_bebidas_calientes_frias(self, temperatura_celsius: int) -> str:
        if temperatura_celsius > self.__temperatura_maxima:
            return f"Alerta: {temperatura_celsius}°C no es compatible con este plástico"
        return f"Compatibilidad exitosa para {temperatura_celsius}°C"

    def cierre_hermetico(self, tipo_sellado: str) -> str:
        return f"Cierre hermético activado usando {tipo_sellado} en la tapa {self.get_tapa()}"

    # ---- EL POLIMORFISMO ----
    def descripcion(self) -> str:
        info_padre = super().descripcion()
        return f"{info_padre} - Flexibilidad: {self.__flexibilidad}"