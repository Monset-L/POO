from Interfaz import *
from tkinter import Tk, Button,random, Frame,messagebox,ttk,Label,Entry

def generar(self):
        for _ in range (1):
            mostrar= random.sample(generar,longitud)
            contraseña = "".join(mostrar)
            print(contraseña)


letras="abcdefghijklmnopqrstuvwxyz"
mayusculas= letras.upper()
numeros="0123456789"
especial="@!¡[]{}*,:_-¿?'.°$%&#"

generar= letras+mayusculas+numeros+especial
longitud= 8

ventana= Tk()
ventana.title("Contraseñas")
ventana.geometry("500x300")

seccion1=Frame(ventana,bg="#9BC1BC")
seccion1.pack(expand=True,fill='both')

Correo= Entry(seccion1)
Correo.place(x=200, y=130)



titulo = Label(text="Generador de contraseñas",fg="Black",font=('Times',30),bg="#9BC1BC")
titulo.place(x=50,y=10)

boton= Button(seccion1,text="Generar",fg="black",bg="#F4F1BB",font=(10),command=generar)
boton.place(x=60,y=20)

ventana.mainloop()