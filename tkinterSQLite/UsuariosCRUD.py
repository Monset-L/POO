from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
from controladorBD import * #Le presentamos la clase a la ventana

#Crear un objeto de tipo controlador
controlador= controladorDB()

#Proceder a guardar usando el metodo del objeto controlador
def ejecutainsert():
    controlador.guardarUsuario(varNom.get(), varCor.get(), varCon.get())


#Funcion para buscar un usuario
def ejecutaSelectU():
    rsUsuario=controlador.consultaUsuario(varBus.get())
    
    for usu in rsUsuario:
        cadena= str(usu[0])+" "+usu[1]+" "+usu[2]+" "+str(usu[3]) #concatenar par hacerla cadena
        
    if(rsUsuario):
        print(cadena)
    else:
        messagebox.showinfo("Id no encontrado","Usuario no registrado en BD")
        
        

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

#Pestaña2:Buscar Usuario
titulo2=Label(pestana2, text="Buscar usuario",fg="green",font=("Modern",18)).pack()

varBus=tk.StringVar()
iblid=Label(pestana2, text="Identificador de Usuario: ").pack()
txtid= Entry(pestana2,textvariable=varBus).pack()

btnBusqueda=Button(pestana2,text="Buscar",command=ejecutaSelectU).pack()

subBus=Label(pestana2,text="Registrado:",fg="blue",font=("Modern",15) ).pack()
textBus=tk.Text(pestana2,height=5,width=52).pack()


panel.add(pestana1,text="Formulario de usuarios")
panel.add(pestana2,text="Buscar usuario")
panel.add(pestana3,text="Consultar usuarios")
panel.add(pestana4,text="Actualizar usuarios")

Ventana.mainloop()