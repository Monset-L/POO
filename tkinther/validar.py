from tkinter import messagebox

class validador:
    
    def __init__(self):
        self.__correo= "coco@gmail.com"
        self.__contraseña= "1234"   
        


    def comprobar(self,Correo,Contraseña):
        if self.__correo == Correo and self.__contraseña == Contraseña:
            messagebox.showinfo("Bienvenido","Ingresaste con éxito :D")
            
        else:
            messagebox.showerror("Error","Llena todos los campos/campos incorrectos\n              intentalo de nuevo.")
 
 
