# se crea la clase padre
class Botella:

    # Crear Canstructor y atributos
    def __init__(self, material: str, capacidad: str, forma: str, diseno: str, tapa: str, grabados: bool):
        self.__material = material
        self.__capacidad = capacidad
        self.__forma = forma
        self.__diseno = diseno
        self.__tapa = tapa
        self.__grabados = grabados

    def get_material(self) -> str:
        return self.__material

    def get_capacidad(self) -> str:
        return self.__capacidad

    def get_forma(self) -> str:
        return self.__forma

    def get_diseno(self) -> str:
        return self.__diseno

    def get_tapa(self) -> str:
        return self.__tapa

    def get_grabados(self) -> bool:
        return self.__grabados

    # Creacion de métodos
    def contener_liquidos(self, liquido: str) -> str:
        return f"La botella de {self.__material} ahora contiene: {liquido}"

    def facilitar_el_vertido(self, angulo_inclinacion: int) -> str:
        return f"Vertiendo líquido eficientemente a un ángulo de {angulo_inclinacion}°"

    def transporte(self, destino: str) -> str:
        return f"Transportando lote de botellas con forma {self.__forma} hacia {destino}"

    def manejo(self, tipo_agarre: str) -> str:
        return f"Manejo de la botella optimizado para agarre de tipo: {tipo_agarre}"

    def grabados_info(self) -> str:
        if self.__grabados:
            return f"La botella de {self.__material} incluye grabados personalizados"
        return f"La botella de {self.__material} no tiene grabados"

    def descripcion(self) -> str:
        return f"Botella generica de {self.__material} - Diseño: {self.__diseno} - Tapa: {self.__tapa}"