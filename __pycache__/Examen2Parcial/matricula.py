import tkinter as tk
from validar import *
import random
from tkinter import Tk, Button, Frame,messagebox,ttk,Label,Entry

def validador ():
    val.comprobar(Correo.get(),Contraseña.get())


ventana= Tk()
ventana.title("Matrícula")
ventana.geometry("600x450")

titulo = Label(text="Generador de matrículas",fg="Black",font=('Times',30))
titulo.place(x=190,y=20)

seccion1=Frame(ventana,bg="#9BC1BC")
seccion1.pack(expand=True,fill='both') 

Carrera= Entry(seccion1)
Carrera.place(x=300, y=130) 
textcarrera = Label(text="Carrera:",fg="Black",font=(8))
textcarrera.place(x=190,y=130)

Anocurso= Entry(seccion1)
Anocurso.place(x=300, y=155) 
textanocurso = Label(text="Año en curso:",fg="Black",font=(8))
textanocurso.place(x=190,y=155)

Anonacimiento= Entry(seccion1)
Anonacimiento.place(x=300, y=180) 
textanonacimiento = Label(text="Fecha de nacimiento:",fg="Black",font=(8))
textanonacimiento.place(x=130,y=180)

Nombre= Entry(seccion1)
Nombre.place(x=300, y=200) 
textnombre= Label(text="Nombre:",fg="Black",font=(8))
textnombre.place(x=130,y=200)

Apellpaterno= Entry(seccion1)
Apellpaterno.place(x=300, y=220) 
textapellidopaterno= Label(text="Apellido paterno:",fg="Black",font=(8))
textapellidopaterno.place(x=130,y=220)

Apellmaterno= Entry(seccion1)
Apellmaterno.place(x=300, y=240) 
textapellidomaterno= Label(text="Apellido materno:",fg="Black",font=(8))
textapellidomaterno.place(x=130,y=240)

boton= Button(seccion1,text="Asignar",fg="black",bg="#F4F1BB",font=(10),command=login)
boton.place(x=280,y=20)

ventana.mainloop()