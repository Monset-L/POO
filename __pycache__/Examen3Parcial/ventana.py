from tkinter import *
from tkinter import ttk,messagebox,Label,Entry
import tkinter as tk
from clase import *

controlador= claseDB()

def ejecutainsert():
    controlador.insertarDatos(varTra.get(),varAdu.get())

Ventana= Tk()
Ventana.title("Exportaciones")
Ventana.geometry("500x300")

panel= ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)

#Pestaña 1 Insertar
titulo=Label(pestana1, text="Insertar exportaciones",fg="Blue",font=("Modern",18)).pack()
varTra= tk.StringVar()
lblTra= Label(pestana1,text="Transporte: ").pack()
txtTra= Entry(pestana1,textvariable=varTra).pack()

varAdu= tk.StringVar()
lblAdu= Label(pestana1,text="Aduana: ").pack()
txtAdu= Entry(pestana1,textvariable=varAdu).pack()
btnGuardar=Button(pestana1,text="Guardar datos",command=ejecutainsert).pack()

#Pestaña 2 Eliminar
titulo5=Label(pestana2, text="Eliminar Datos",fg="green",font=("Modern",18)).pack()

VarElid=tk.StringVar()
Eid=Label(pestana2,text='ID: ')
Eid.place(x=160,y=40)
Elid= tk.Entry(pestana2,textvariable=VarElid)
Elid.place(x=220,y=40)

btnEliminar=Button(pestana2,text="Eliminar")
btnEliminar.place(x=220, y=80)


panel.add(pestana1,text="Insertar Datos")
panel.add(pestana2,text="Eliminar Datos")
panel.add(pestana3,text="Consultar Datos por Aduana")







Ventana.mainloop()