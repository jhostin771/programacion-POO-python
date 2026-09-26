from botella import Botella 

class BotellaVidrio(Botella):
    def __init__(self):
        super().__init__()
        self.transparencia = " "
        self.reciclable = " "

    def asignacion_vidrio(self):
        super().asignacion_datos("Vidrio", "750ml", "Cilindrica")
        self.transparencia = "Alta"
        self.reciclable = "Si"