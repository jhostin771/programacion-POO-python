# Solucion para que muestre las tildes y las ñ
import sys
sys.stdout.reconfigure(encoding='utf-8')

from carro import Carro
from van import Van
from camion import Camion

#*********************** CODIGO PRINCIPAL ****************************
# Creacion de objetos
carro_bmw = Carro("BMW Z4", "Negro", "V6", 2, "Gasolina", "LED", "Automatica")
van_carga = Van("Chevrolet N300", "Blanco", "1.2L", 4, "Gasolina", "halógenas", 8)
camion_basura = Camion("Hino 500", "Blanco", "Diesel 4.0L", 2, "Diesel", "halógenas", 8000, "Frenos ABS")

# llamado de Metodos
# ---- El Carro ----
print(carro_bmw.descripcion())
print(carro_bmw.luces())
print(carro_bmw.climatizar(22))

print("-" * 50)

# ---- La Van ----
print(van_carga.descripcion())
print(van_carga.luces())
print(van_carga.pasajeros_info(10))
print(van_carga.espejos("Ajustando"))

print("-" * 50)

# ---- El Camion ----
print(camion_basura.descripcion())
print(camion_basura.luces())
print(camion_basura.cargar(9000))
print(camion_basura.seguridad_info())