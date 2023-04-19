from tkinter import messagebox,ttk
import sqlite3
import bcrypt

class claseDB:
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion= sqlite3.connect("C:/Users/lupit/Documents/uni/Cuatri 5/POO/github/POO/tkinterSQLite/BDExportaciones.db")   
            print("Conectado BD") 
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar")


    def insertarDatos(self,Tra,Adu):
        conx= self.conexionBD()
        if(Tra == "" or Adu==""):
            messagebox.showwarning("Cuidado!", "Revisa todos los campos")
            conx.close()
        else:
            cursor= conx.cursor()
            datos=(Tra,Adu)
            qrInsert="insert into TBPedimentos(Transporte, Aduana)values(?,?) "
            
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Éxito","Se guardaron los datos")
    