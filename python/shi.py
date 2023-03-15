from tkinter import Tk, Button, Frame,messagebox,ttk,Label,Entry
import tkinter as tk

Interfaz=Tk()

class Electrodomestico:
    def __init__(self, nombre, marca, color, peso, precio):
        self.nombre = nombre
        self.marca = marca
        self.color = color
        self.peso = peso
        self.precio = precio
        
class App:
    def __init__(self, master):
        self.master = master
        master.title("Gestión de activos de Electrodomésticos")

        # Creamos el marco principal
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        # Creamos los widgets para el ingreso de datos
        self.nombre_label = tk.Label(self.frame, text="Nombre:")
        self.nombre_label.grid(row=0, column=0)
        self.nombre_entry = tk.Entry(self.frame)
        self.nombre_entry.grid(row=0, column=1)

        self.marca_label = tk.Label(self.frame, text="Marca:")
        self.marca_label.grid(row=1, column=0)
        self.marca_entry = tk.Entry(self.frame)
        self.marca_entry.grid(row=1, column=1)

        self.color_label = tk.Label(self.frame, text="Color:")
        self.color_label.grid(row=2, column=0)
        self.color_entry = tk.Entry(self.frame)
        self.color_entry.grid(row=2, column=1)

        self.peso_label = tk.Label(self.frame, text="Peso:")
        self.peso_label.grid(row=3, column=0)
        self.peso_entry = tk.Entry(self.frame)
        self.peso_entry.grid(row=3, column=1)

        self.precio_label = tk.Label(self.frame, text="Precio:")
        self.precio_label.grid(row=4, column=0)
        self.precio_entry = tk.Entry(self.frame)
        self.precio_entry.grid(row=4, column=1)

        # Creamos los botones para guardar, buscar y vender electrodomésticos
        self.guardar_button = tk.Button(self.frame, text="Guardar", command=self.guardar)
        self.guardar_button.grid(row=5, column=0)

        self.buscar_button = tk.Button(self.frame, text="Buscar", command=self.buscar)
        self.buscar_button.grid(row=5, column=1)

        self.vender_button = tk.Button(self.frame, text="Vender", command=self.vender)
        self.vender_button.grid(row=5, column=2)

        # Creamos el área de texto para mostrar la información de los electrodomésticos
        self.text_area = tk.Text(self.frame, height=10, width=50)
        self.text_area.grid(row=6, columnspan=3)

        # Inicializamos la lista de electrodomésticos
        self.electrodomesticos = []

    # Función para guardar un electrodoméstico
    def guardar(self):
        electrodomestico = Electrodomestico(
            self.nombre_entry.get(),
            self.marca_entry.get(),
            self.color_entry.get(),
            float(self.peso_entry.get()),
            float(self.precio_entry.get())
        )
        self.electrodomesticos.append(electrodomestico)
        self.text_area.insert(tk.END, "Electrodoméstico guardado:\n")
        self.text_area.insert(tk.END, str(electrodomestico.__dict__) + "\n\n")

    # Función para buscar


tk.mainloop()