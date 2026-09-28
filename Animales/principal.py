import sys
sys.stdout.reconfigure(encoding='utf-8')

from caballo import Caballo
from cocodrilo import Cocodrilo
from pez import Pez
from escarabajo import Escarabajo
from pato import Pato

#*********************** CODIGO PRINCIPAL ****************************
# Creacion de objetos
caballo = Caballo("Caballo", "el campo", "pasto", "Marron", "1.6 m de alto", 30, "galopando", "criolla")
cocodrilo = Cocodrilo("Cocodrilo", "el río", "peces y carne", "Verde", "4 m de largo", 70, "caminando y nadando", 70)
pez = Pez("Pez", "el acuario", "algas", "Naranja", "15 cm de largo", 5, "nadando", "dulce")
escarabajo = Escarabajo("Escarabajo", "el bosque", "hojas y frutas", "Negro", "6 cm de largo", 2, "caminando y volando", True)
pato = Pato("Pato", "la laguna", "semillas y plantas", "Verde", "60 cm de largo", 20, "nadando y volando", 10)

# llamado de Metodos
# ---- Caballo ----
print(caballo.descripcion())
print(caballo.alimentarse())
print(caballo.moverse())
print(caballo.vida_y_tamano())
print(caballo.relinchar())

print("-" * 50)

# ---- Cocodilo ----
print(cocodrilo.descripcion())
print(cocodrilo.alimentarse())
print(cocodrilo.moverse())
print(cocodrilo.vida_y_tamano())
print(cocodrilo.morder())

print("-" * 50)

# ---- Pez ----
print(pez.descripcion())
print(pez.alimentarse())
print(pez.moverse())
print(pez.vida_y_tamano())
print(pez.nadar_en_grupo(5))

print("-" * 50)

# ---- Escarabajo ----
print(escarabajo.descripcion())
print(escarabajo.alimentarse())
print(escarabajo.moverse())
print(escarabajo.vida_y_tamano())
print(escarabajo.pelear())

print("-" * 50)

# ---- Pato ----
print(pato.descripcion())
print(pato.alimentarse())
print(pato.moverse())
print(pato.vida_y_tamano())
print(pato.graznar())