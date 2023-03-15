from tkinter import Tk, Button, Frame,messagebox,ttk,Label,Entry
import tkinter as tk

Interfaz=Tk()

class Interfaz_Electrodomesticos:
    
    def __init__(self,master):
        self.master= master
        master.title("Gestión de activos de electrodomésticos")
        
        self.etiqueta_nombre = Label(master, text="Nombre:")
        self.entrada_nombre = Entry(master)
        
        self.etiqueta_marca = Label(master,text="Marca:")
        self.entrada_marca = Entry(master)
        
        self.etiqueta_color = Label(master,text="Color:")
        self.entrada_color = Entry(master)
        
        self.etiqueta_peso = Label(master,text="Peso:")
        self.entrada_peso = Entry(master)
        
        self.etiqueta_precio = Label(master,text="Precio:")
        self.entrada_precio = Entry(master)
        
        self.boton_registrar = Button(master, text="Registrar electrodoméstico", command=self.registrar_electrodomestico)
        self.boton_consultar = Button(master, text="Consultar electrodomésticos", command=self.boton_consultar_electrodomesticos)
        
        self.boton_vender = Button(master, text="Vender electrodoméstico", command=self.vender_electrodomestico)
        self.boton_salir = Button(master, text="Salir", command=master.quit)
        
        
        self.etiqueta_nombre.grid(row=0, column=0)
        self.entrada_nombre.grid(row=0, column=1)
        
        self.etiqueta_marca.grid(row=1,column=0)
        self.entrada_marca.grid(row=1,column=1)
        
        self.etiqueta_color.grid(row=2,column=0)
        self.entrada_color.grid(row=2,column=1)
        
        self.etiqueta_peso.grid(row=3,column=0)
        self.entrada_peso.grid(row=3,column=1)
        
        self.etiqueta_precio.grid(row=4,column=0)
        self.entrada_precio.grid(row=4,column=1)
        
        self.boton_registrar.grid(row=5, column=0)
        self.boton_consultar.grid(row=5, column=1)
        self.boton_vender.grid(row=6, column=0)
        self.boton_salir.grid(row=6, column=1)
        
    def registrar_electrodomestico(self):
        nombre = self.entrada_nombre.get()
        marca = self.entrada_marca.get()
        color = self.entrada_color.get()
        peso = self.entrada_peso.get()
        precio = self.entrada_precio.get()
        
        if nombre and marca and color and peso and precio:
            messagebox.showinfo("Campos vacios")
            
            
tk.mainloop()