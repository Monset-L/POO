from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorBD import * #Le presentamos la clase a la ventana

#Crear un objeto de tipo controlador
controlador= controladorDB()

#Proceder a guardar usando el metodo del objeto controlador
def ejecutainsert():
    controlador.guardarUsuario(varNom.get(), varCor.get(), varCon.get())


Ventana= Tk()
Ventana.title("CRUD Usuarios")
Ventana.geometry("500x300")

panel= ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)

#Pestana1: Formulario de usuarios
titulo=Label(pestana1, text="Registro de usuarios",fg="Blue",font=("Modern",18)).pack()
varNom= tk.StringVar()
lblNom= Label(pestana1,text="Nombre: ").pack()
txtNom= Entry(pestana1,textvariable=varNom).pack()

varCor= tk.StringVar()
lblCor= Label(pestana1,text="Correo: ").pack()
txtCor= Entry(pestana1,textvariable=varCor).pack()

varCon= tk.StringVar()
lblCon= Label(pestana1,text="Contraseña: ").pack()
txtCon= Entry(pestana1,textvariable=varCon).pack()

btnGuardar=Button(pestana1,text="Guardar usuario",command=ejecutainsert).pack()

panel.add(pestana1,text="Formulario de usuarios")
panel.add(pestana2,text="Buscar usuario")
panel.add(pestana3,text="Consultar usuarios")
panel.add(pestana4,text="Actualizar usuarios")

Ventana.mainloop()