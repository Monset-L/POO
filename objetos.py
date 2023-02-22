
from Personaje import *

#1.Solicitar datos

print("")
print("######### Datos Heroe ########")
especieH=input("Escribe la especie del Heroe: ")
nombreH=input("Escribe el nombre del Heroe: ")
alturaH=float(input("Escribe la altura del Heroe: "))
recargarH=int(input("Cuantas balas recargas al Heroe: "))

print("")
print("######### Datos Villano ########")
especieV=input("Escribe la especie del Villano: ")
nombreV=input("Escribe el nombre del Villano: ")
alturaV=float(input("Escribe la altura del Villano: "))
recargarV=int(input("Cuantas balas recargas al Villano: "))

#2.Crear objeto de clase Personaje

heroe= Personaje(especieH,nombreH,alturaH)
villano= Personaje(especieV,nombreV,alturaV)

#3.Usar atributos

print("")
print("######### Objeto Heroe ########")
print("El personaje se llama: "+ heroe.nombre)
print("Pertenece a la especie: "+ heroe.especie)
print("y tiene una altura de: "+ str(heroe.altura))

heroe.correr(False)
heroe.lanzarGranadas()
heroe.recargarArma(recargarV)


print("")
print("######### Objeto Villano ########")
print("El personaje se llama: "+ villano.nombre)
print("Pertenece a la especie: "+ villano.especie)
print("y tiene una altura de: "+ str(villano.altura))


villano.correr(False)
villano.lanzarGranadas()
villano.recargarArma(recargarV)
