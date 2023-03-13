import tkinter as tk
from tkinter import Tk, Button, Frame,messagebox,ttk,Label,Entry
from Formulario import *


login=Tk()
#seccion1=Frame(login,bg="#9BC1BC")
#seccion1.pack(expand=True,fill='both')


def crear_login():
    global saldo
    global login
    login.title("Caja Popular")
    login.geometry("300x300")
    titulo = Label(text="Caja Popular",fg="Black",font=('Times',30),bg="#9BC1BC")
    titulo.place(x=40,y=25)
    
    tk.Label(login,text="Usuario/Titular").place(x=30, y=100)
    tk.Entry(login, textvariable=titular).place(x=120, y=100)
    tk.Label(login, text="Password").place(x=40, y=130)
    tk.Entry(login, textvariable=passw).place(x=120, y=130)
    tk.Button(login,text="Ingresar", command=validar_usuario).place(x=130, y=160)



def validar_usuario():
    usuario_def = 'lili'
    pass_def = '1234'

    if(usuario_def == titular.get() and pass_def == passw.get()):
        messagebox.showinfo("Bienvenido","Ingresaste con éxito :D")
        menu_opciones()
    else: 
        messagebox.showerror("Error", "Usuario o contraseña incorrectos\n     Intentalo de nuevo")

def menu_opciones():
    global menu
    menu = tk.Tk()
    menu.title("Opciones a realizar")
    menu.geometry("300x300")
    titulo = Label(text="Opciones",fg="Black",font=('Times',30),bg="#9BC1BC")
    titulo.place(x=40,y=25)
    
    tk.Button(menu, text="Depositar",fg="black",bg="#F4F1BB",font=(10),command=depositar).place(x=30, y=60)
    tk.Button(menu, text="Retirar",fg="black",bg="#F4F1BB",font=(10),command=retirar).place(x=30, y=120)
    tk.Button(menu, text="Consultar",fg="black",bg="#F4F1BB",font=(10),command=consultar).place(x=30, y=180)
    #tk.Button(menu, text="DepositaraCuenta",command=depositarCuenta).place(x=180, y=120)
    login.iconify()

def retirar():
    global retiro_menu
    global saldo
    retiro_menu = tk.Tk()
    retiro_menu.title("Retiro")
    retiro_menu.geometry("300x300")
    titulo = Label(text="Retirar en cuenta",fg="Black",font=('Times',30),bg="#9BC1BC")
    titulo.place(x=40,y=25)
    
    tk.Label(retiro_menu,text="Saldo disponible",font=10).place(x=50, y=50)
    label = tk.Label(retiro_menu, text=str (saldo.get()))
    label.place(x=200, y=50)
    entry = tk.Entry(retiro_menu,textvariable=cantidad)
    entry.place(x=150, y=80)
    tk.Button(retiro_menu, text="Retirar",fg="black",bg="#F4F1BB",font=(10), command=lambda:[get_retirar(entry.get()),actualizar_label(label)]).place(x=50, y=80)
    tk.Button(retiro_menu, text="Atrás",fg="black",bg="#ABBCFF",font=(10), command=lambda:regresar_menu(retiro_menu)).place(x=200, y=200)
    menu.iconify()



def depositar():
    global deposito_menu
    global saldo
    deposito_menu = tk.Tk()
    deposito_menu.title("Deposito")
    deposito_menu.geometry("300x300")
    titulo = Label(text="Depositar en cuenta",fg="Black",font=('Times',30),bg="#9BC1BC")
    titulo.place(x=40,y=25)
    
    tk.Label(deposito_menu,text="Saldo disponible",font=10).place(x=50, y=50)
    label=tk.Label(deposito_menu, text=str(saldo.get()))
    label.place(x=200, y=50)
    entry = tk.Entry(deposito_menu, textvariable=cantidad)
    entry.place(x=150, y=80)
    tk.Button(deposito_menu, text="Depositar",fg="black",bg="#F4F1BB",font=(10), command=lambda:[set_depositar(entry.get()),actualizar_label(label)]).place(x=50, y=80)
    tk.Button(deposito_menu, text="Atrás",fg="black",bg="#ABBCFF",font=(10), command=lambda:regresar_menu(deposito_menu)).place(x=200, y=200)
    menu.iconify()

def consultar():
    global consulta_menu
    global saldo
    consulta_menu = tk.Tk()
    consulta_menu.title("Consulta")
    consulta_menu.geometry("300x300")
    tk.Label(consulta_menu,text="Saldo disponible",font=10).place(x=50, y=50)
    label=tk.Label(consulta_menu, text=str(saldo.get()))
    label.place(x=200, y=50)
    tk.Button(consulta_menu, text="Atrás",fg="black",bg="#ABBCFF",font=(10), command=lambda:regresar_menu(consulta_menu)).place(x=200, y=200)
    menu.iconify()

def get_retirar(valor):
    global saldo
    if((saldo.get()-float(valor))<0):
        messagebox.showinfo("Error", "Saldo insuficiente")
    else:
        total = saldo.get()
        total -= float(valor)
        saldo.set(round(total,2))
        messagebox.showinfo("Éxito", "Retiro realizado correctamente")

def set_depositar(valor):
    global saldo
    total = saldo.get()
    total += float(valor)
    saldo.set(round(total,2))
    messagebox.showinfo("Éxito", "Depósito realizado correctamente")

def regresar_login():
    menu.iconify()
    login.deiconify()

def regresar_menu(label):
    menu.iconify()
    menu.deiconify()
    
def actualizar_label(label):
    global saldo
    label.config(text= saldo.get())
    
crear_login()

tk.mainloop()