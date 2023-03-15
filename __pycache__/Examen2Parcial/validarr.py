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
        matricula = ""
        ano_actual = str(2023)[-2:]
        ano_nacimiento =  str(self.ano_nacimiento)[-2:]
        primera_letra_nombre = self.nombre[0]
        tres_letras_apellido_paterno = self.apellido_paterno[:3]
        tres_letras_apellido_materno = self.apellido_materno[:3]
        tres_primeras_letras_carrera = self.carrera[:3]
        tres_digitos_aleatorios = str(random.randint(100, 999))
            
        matricula = tres_primeras_letras_carrera + ano_actual + ano_nacimiento + primera_letra_nombre + tres_letras_apellido_paterno + tres_letras_apellido_materno + tres_digitos_aleatorios
            
        return matricula
    
matricula_generada = matricula.generar_matricula()

matricula_generada = (messagebox.showinfo("Tu matrícula es: ",matricula_generada))
