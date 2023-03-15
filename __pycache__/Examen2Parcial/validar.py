from tkinter import messagebox
import random

class validador:
    class matricula():
        def __init__(self,nombre,apellido_paterno, apellido_materno,ano_nacimiento, carrera):
            self.nombre = nombre
            self.apellido_paterno = apellido_paterno
            self.apellido_materno = apellido_materno
            self.ano_nacimiento = ano_nacimiento
            self.carrera = carrera

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