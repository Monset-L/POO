import tkinter as tk
from validar import *
from tkinter import Tk, Button, Frame,messagebox,ttk,Label,Entry

def login ():
    val.comprobar(Correo.get(),Contraseña.get())
    
    
val = validador()    

ventana= Tk()
ventana.title("Login")
ventana.geometry("600x450")

seccion1=Frame(ventana,bg="#9BC1BC")
seccion1.pack(expand=True,fill='both') 

seccion2=Frame(ventana,bg="#E6EBE0")
seccion2.pack(expand=True,fill='both')

 

 
# Caja de texto.

titulo = Label(text="Inicio de sesión",fg="Black",font=('Times',30),bg="#9BC1BC")
titulo.place(x=190,y=20)

Correo= Entry(seccion1)
Correo.place(x=300, y=130) 

Contraseña= Entry(seccion1)
Contraseña.configure(show="*")
Contraseña.place(x=300, y=180) 

textcorreo = Label(text="Correo:",fg="Black",font=(8))
textcorreo.place(x=190,y=130)

textcontraseña = Label(text="Contraseña:",fg="Black",font=(8))
textcontraseña.place(x=180,y=180)

#Botón
boton= Button(seccion2,text="Ingresar",fg="black",bg="#F4F1BB",font=(10),command=login)
boton.place(x=280,y=20)


ventana.mainloop()