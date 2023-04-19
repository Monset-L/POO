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
    
    def EliminarDatos(self,id):
        conx =self.conexionBD()
        if(id == ""):
            messagebox.showwarning("Cuidado", "Id vacio escribe uno valido")
            conx.close()
        else:
            try:
                cursor = conx.cursor()
                sqlDelte = ("DELETE FROM TBPedimentos WHERE IDExpo = ?")
                dato=(id)
                Mensaje= messagebox.askokcancel("Cuidado", "Está seguro de que desea eliminar los datos?")
                if Mensaje == True:
                    cursor.execute(sqlDelte,dato)
                    conx.commit()
                    conx.close()
                    messagebox.showinfo("Eliminado","Se eliminaron los datos")
                else:
                    conx.close()
                    messagebox.showerror("Algo falló","Ningún dato eliminado")
            
            except sqlite3.OperationalError:
                    print("Error Consulta")
                    
    
    def consultaDato(self,Adu):
        conx= self.conexionBD()
        if(Adu == ""):
            messagebox.showwarning("Cuidado", "Campo vacio escribe uno valido")
            conx.close()
        else:
            try:
                cursor= conx.cursor()
                sqlSelect="select * from TBPedimentos where Aduana="+Adu
                
                cursor.execute(sqlSelect)
                RSusuario = cursor.fetchall()
                conx.close()
                return RSusuario
            except sqlite3.OperationalError:
                print("Error Consulta")