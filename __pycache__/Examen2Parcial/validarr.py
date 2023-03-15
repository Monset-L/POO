from tkinter import messagebox
import random
    
class matricula():
    def __init__(self,Carrera,Anonacimiento, Nombre,Apellpaterno,Apellmaterno):
        self.nombre = Nombre
        self.apellido_paterno = Apellpaterno
        self.apellido_materno = Apellmaterno
        self.ano_nacimiento = Anonacimiento
        self.carrera = Carrera

    def generar_matricula(self):
        self.ano_actual = str(2023)[-2:]
        self.ano_nacimiento =  str(self.ano_nacimiento)[-2:]
        self.primera_letra_nombre = self.nombre[0]
        self.tres_letras_apellido_paterno = self.apellido_paterno[:3]
        self.tres_letras_apellido_materno = self.apellido_materno[:3]
        self.tres_primeras_letras_carrera = self.carrera[:3]
        self.tres_digitos_aleatorios = str(random.randint(100, 999))
            
        self.matricula =str(self.tres_primeras_letras_carrera + self.ano_actual + self.ano_nacimiento + self.primera_letra_nombre + self.tres_letras_apellido_paterno + self.tres_letras_apellido_materno + self.tres_digitos_aleatorios)
            
        self.matricula_generada = messagebox.showinfo("Generada con exito","Tu matrícula es: " + self.matricula)
    



