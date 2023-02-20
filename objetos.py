
from Personaje import *

#1.Crear objeto de clase Personaje

heroe= Personaje()

#2.Usar atributos

print("El personaje se llama: "+ heroe.nombre)
print("pertenece a la especie: "+ heroe.especie)
print("y tiene una altura de: "+ heroe.altura)

#3.Usar metodos

heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(87)