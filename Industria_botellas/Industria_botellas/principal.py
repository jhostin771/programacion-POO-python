# Esto si no lo enseño pero es una solucion que encontre para que muestre las tildes y las ñ
import sys
sys.stdout.reconfigure(encoding='utf-8')

from botella_vidrio import BotellaVidrio
from botella_plastico import BotellaPlastico

#*********************** CODIGO PRINCIPAL ****************************
# Creacion de objetos
botella_gaseosa = BotellaVidrio("Vidrio", "350ml", "Cilindrica", "Retro", "Corona metalica", True, 85, 20)
botella_agua = BotellaPlastico("Plastico", "500ml", "Rectangular", "Deportivo", "Rosca", False, "Media", 60)

# llamdo de Métodos 
print(botella_gaseosa.descripcion())
print(botella_gaseosa.contener_liquidos("Gaseosa"))
print(botella_gaseosa.grabados_info())
print(botella_gaseosa.transparencia_info(85))
print(botella_gaseosa.reutilizacion(15))

print("-" * 50)

print(botella_agua.descripcion())
print(botella_agua.contener_liquidos("Agua"))
print(botella_agua.grabados_info())
print(botella_agua.compatibilidad_con_bebidas_calientes_frias(70))
print(botella_agua.cierre_hermetico("Rosca doble"))