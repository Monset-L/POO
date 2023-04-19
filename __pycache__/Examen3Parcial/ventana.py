from tkinter import *
from tkinter import ttk,messagebox,Label,Entry
import tkinter as tk
from clase import *

controlador= claseDB()

def ejecutainsert():
    controlador.insertarDatos(varTra.get(),varAdu.get())
    
def ejecutarEliminar(): 
    controlador.EliminarDatos(Varid.get())
    
def ejecutaConsultaA():
    for i in textBu.get_children():
        textBu.delete(i)
        
    rsUsuario=controlador.consultaDato(varCon.get())
    
    for usu in rsUsuario:
        
        cadena= str(usu[0])+" "+usu[1]+" "+usu[2]    #concatenar par hacerla cadena
        
    if(rsUsuario):
        textBu.insert("",0,values=cadena)
    
    else:
        messagebox.showinfo("Id no encontrado","Usuario no registrado en BD")

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

Varid=tk.StringVar()
Elid=Label(pestana2,text='ID: ')
Elid.place(x=160,y=40)
Elmid= tk.Entry(pestana2,textvariable=Varid)
Elmid.place(x=220,y=40)

btnEliminar=Button(pestana2,text="Eliminar",command=ejecutarEliminar)
btnEliminar.place(x=220, y=80)





#Pestaña 3 Consultar Aduana
titulo2=Label(pestana3, text="Consultar Aduana",fg="green",font=("Modern",18)).pack()

varCon=tk.StringVar()
iblAdu=Label(pestana3, text="Identificador de Usuario: ").pack()
txtAdu= Entry(pestana3,textvariable=varCon).pack()

btnBusqueda=Button(pestana3,text="Consultar",command=ejecutaConsultaA).pack()

subBus=Label(pestana3,text="Registrados:",fg="blue",font=("Modern",15) ).pack()
textBu=ttk.Treeview(pestana3,columns=('#0','#1','#2'))
textBu.heading("#1",text="ID",anchor=CENTER)
textBu.heading("#2",text="Transporte",anchor=CENTER)
textBu.heading("#3",text="Aduana",anchor=CENTER)


textBu.column("#0",width=1)
textBu.column("#1",width=20)
textBu.column("#2",width=100)


textBu.pack()         




panel.add(pestana1,text="Insertar Datos")
panel.add(pestana2,text="Eliminar Datos")
panel.add(pestana3,text="Consultar Datos por Aduana")
Ventana.mainloop()