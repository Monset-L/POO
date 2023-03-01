from tkinter import Tk, Button, Frame,messagebox

#5.Declaramos funciones
def mostrarMensajes():
    messagebox.showinfo("Aviso:", "Presionaste el botón negro")
    messagebox.showerror("Error","Todo falló con éxito")
    print(messagebox.askokcancel("Pregunta","¿Te gusta el sabor a chocolate?"))
    print(messagebox.askyesnocancel("Pregunta","¿Te gusta el sabor a chocolate?"))
    print(messagebox.askyesno("Pregunta","¿Te gusta el sabor a chocolate?"))
    
#6. Funcion para agregar botones
def agregarBoton():
    botonVerde.config(text="+",bg="green",fg="white")
    botonNuevo=Button(seccion3,text="Nuevo")
    botonNuevo.pack()

#1.Instanciamos el objeto ventana (Creación de un objeto)
ventana= Tk()
ventana.title("Ejemplo de 3 Frames")
ventana.geometry("600x400")

#2.Agregamos los Frames
seccion1=Frame(ventana,bg="red")
seccion1.pack(expand=True,fill='both') 

seccion2=Frame(ventana,bg="white")
seccion2.pack(expand=True,fill='both')

seccion3=Frame(ventana,bg="grey")
seccion3.pack(expand=True,fill='both')

#3.Agregamos botones
botonNegro= Button(seccion1,text="Boton Negro",fg="white",bg="black",command=mostrarMensajes)
botonNegro.place(x=60,y=60)


botonRosa= Button(seccion2,text="Boton Rosa",fg="white",bg="#F26767")
botonRosa.grid(row=0, column=0)

botonAzul= Button(seccion2,text="Boton Azul",fg="blue")
botonAzul.grid(row=1, column=1)

botonVerde= Button(seccion3,text="Boton Verde",fg="white",bg="#38B35B",command=agregarBoton)
botonVerde.configure(height=2, width=10)
botonVerde.pack()

#llamamos al Main (el mainloop, necesita estar hasta abajo en el código)
ventana.mainloop()