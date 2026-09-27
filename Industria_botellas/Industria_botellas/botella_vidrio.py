# --------- Clases Hijas ---------
from botella import Botella

class BotellaVidrio(Botella):

    def __init__(self, material: str, capacidad: str, forma: str, diseno: str, tapa: str, grabados: bool,
                 transparencia: int, veces_maximas_reutilizable: int):
        super().__init__(material, capacidad, forma, diseno, tapa, grabados)
        # ---- Aqui esta el encapsulamiento ya que son atributos privados y solo se acceden con el get ----
        self.__transparencia = transparencia
        self.__veces_maximas_reutilizable = veces_maximas_reutilizable

    def get_transparencia(self) -> int:
        return self.__transparencia

    def transparencia_info(self, porcentaje_luz: int) -> str:
        return f"Transparencia del vidrio permite el paso del {porcentaje_luz}% de luz"

    def reutilizacion(self, veces_reutilizada: int) -> str:
        apto = veces_reutilizada <= self.__veces_maximas_reutilizable
        return f"¿Apta para reutilizar {veces_reutilizada} veces?: {apto}"

    # ---- Aqui el polimorfismo ya que cada botella lo describe como quiere ----
    def descripcion(self) -> str:
        info_padre = super().descripcion()
        return f"{info_padre} - Transparencia: {self.__transparencia}%"