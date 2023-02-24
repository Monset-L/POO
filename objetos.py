
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
heroe.setNombre(" Pepe pecas ")     #Cambiar el atributo por medio del set, ignorando lo demás 

print("")
print("######### Objeto Heroe ########")
print("El personaje se llama: "+ heroe.getNombre())
print("Pertenece a la especie: "+ heroe.getEspecie())
print("y tiene una altura de: "+ str(heroe.getAltura()))

heroe.correr(False)
heroe.lanzarGranadas()
heroe.recargarArma(recargarV)
heroe.__pensar()


print("")
print("######### Objeto Villano ########")
print("El personaje se llama: "+ villano.getNombre())
print("Pertenece a la especie: "+ villano.getEspecie())
print("y tiene una altura de: "+ str(villano.getAltura()))


villano.correr(False)
villano.lanzarGranadas()
villano.recargarArma(recargarV)
