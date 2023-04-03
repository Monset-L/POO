from tkinter import *
from tkinter import ttk,messagebox,Label,Entry
import tkinter as tk
from controladorBD import * #Le presentamos la clase a la ventana

#Crear un objeto de tipo controlador
controlador= controladorDB()

#Proceder a guardar usando el metodo del objeto controlador
def ejecutainsert():
    controlador.guardarUsuario(varNom.get(), varCor.get(), varCon.get())


#Funcion para buscar un usuario
def ejecutaSelectU():
    for i in textBus.get_children():
        textBus.delete(i)
        
    rsUsuario=controlador.consultaUsuario(varBus.get())
    
    for usu in rsUsuario:
        
        cadena= str(usu[0])+" "+usu[1]+" "+usu[2]+" "+str(usu[3]) #concatenar par hacerla cadena
        
    if(rsUsuario):
        textBus.insert("",0,values=cadena)
    
    else:
        messagebox.showinfo("Id no encontrado","Usuario no registrado en BD")
      
      
#Función consultar usuario       
def ejecutarSelectCU():
    for i in TablaC.get_children():
        TablaC.delete(i)
        
    consultar= controlador.ConsultarUsuario()   
     
    for datos in consultar:
        TablaC.insert("",tk.END, text="",values=datos)

    
Ventana= Tk()
Ventana.title("CRUD Usuarios")
Ventana.geometry("500x300")

panel= ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)
pestana5= ttk.Frame(panel)

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
textBus=ttk.Treeview(pestana2,columns=('#0','#1','#2','#3'))
textBus.heading("#1",text="ID",anchor=CENTER)
textBus.heading("#2",text="Nombre",anchor=CENTER)
textBus.heading("#3",text="Correo",anchor=CENTER)
textBus.heading("#4",text="Contraseña",anchor=CENTER) 

textBus.column("#0",width=1)
textBus.column("#1",width=20)
textBus.column("#2",width=100)
textBus.column("#3",width=150)
textBus.column("#4",width=150)
textBus.pack()              #Aqui se tiene que mostrar el id 

  
#Panel consultar usuarios
titulo3=Label(pestana3, text="Consultar usuarios",fg="green",font=("Modern",18)).pack()
btnBusqueda=Button(pestana3,text="Consultar",command=ejecutarSelectCU).pack()
columns=("id","nombre","correo","contraseña")
TablaC= ttk.Treeview(pestana3,columns=columns,show ="headings")

TablaC.heading("id",text="ID",anchor=CENTER)
TablaC.heading("nombre",text="Nombre",anchor=CENTER)
TablaC.heading("correo",text="Correo",anchor=CENTER)
TablaC.heading("contraseña",text="Contraseña",anchor=CENTER) 

TablaC.column("id",anchor=tk.W,width=1)
TablaC.column("nombre",anchor=tk.W,width=100)
TablaC.column("correo",anchor=tk.W,width=150)
TablaC.column("contraseña",anchor=tk.W,width=180)

TablaC.pack()



#Pestaña 4 Actualizar usuarios
titulo4=Label(pestana4, text="Actualizar usuario",fg="green",font=("Modern",18)).pack()

Iid=Label(pestana4,text='ID: ')
Iid.place(x=160,y=40)
nid= tk.Entry(pestana4)
nid.place(x=220,y=40)

Nnomb=Label(pestana4, text='Nombre: ')
Nnomb.place(x=160, y=80)
nnombre=tk.Entry(pestana4)
nnombre.place(x=220, y=80)

Ncorre= Label(pestana4, text='Correo: ')
Ncorre.place(x=160, y=120)
ncorreo=tk.Entry(pestana4)
ncorreo.place(x=220, y=120)

Ncontr= Label(pestana4, text='Contraseña: ')
Ncontr.place(x=150, y=160)
ncontraseña=tk.Entry(pestana4)
ncontraseña.place(x=220, y=160)

btnActualizar=Button(pestana4,text="Actualizar")
btnActualizar.place(x=220, y=200)

#Pestaña 5 Eliminar usuarios
titulo5=Label(pestana5, text="Eliminar usuario",fg="green",font=("Modern",18)).pack()



panel.add(pestana1,text="Registro de usuarios")
panel.add(pestana2,text="Buscar usuario")
panel.add(pestana3,text="Consultar usuarios")
panel.add(pestana4,text="Actualizar usuario")
panel.add(pestana5,text="Eliminar usuario")


Ventana.mainloop()