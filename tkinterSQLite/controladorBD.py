from tkinter import messagebox,ttk
import sqlite3
import bcrypt

class controladorDB:
    def __init__(self):
        pass
    
    #1. Preparamos la conexión para usarla cuando sea necesario
    def conexionBD(self):
        try:
            conexion= sqlite3.connect("C:/Users/lupit/Documents/uni/Cuatri 5/POO/github/POO/tkinterSQLite/DBUsuarios.db")   
            print("Conectado BD") 
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
            
    def guardarUsuario(self, nom, cor, con):
        
        #1. Llamar a la conexión 
        conx= self.conexionBD()
        
        #2. Revisar que los parámetros no estén vacios
        if(nom == "" or cor=="" or con==""):
            messagebox.showwarning("Aguas!!", "Revisa tu formulario")
            conx.close()
        else:
            #3. Insertar,Preparamos los datos y el querySQL
            cursor= conx.cursor()
            conH= self.encryptarCon(con)
            datos=(nom,cor,conH)
            qrInsert="insert into TBRegistrados(nombre, correo, contraseña)values(?,?,?) "
            
            #4. Proceder a insertar y cerramos la conexión
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Éxito","Se guardó el usuario")
            
    def encryptarCon (self,con):
        conPlana= con
        conPlana= conPlana.encode()  #Convertimos con a bytes
        sal= bcrypt.gensalt()
        conHa= bcrypt.hashpw(conPlana, sal)
        
        print(conHa)
        return conHa
    
    def consultaUsuario(self,id):  #Método
        #1. Preparo la conexión
        conx= self.conexionBD()
        
        #2.Verificar el id no esté vacio
        if(id == ""):
            messagebox.showwarning("Cuidado", "Id vacio escribe uno valido")
            conx.close()
        else:
            #3. Proceder a buscar
            try:
                #4. Preparar lo necesario para el select
                cursor= conx.cursor()
                sqlSelect="select * from TBRegistrados where id="+id
                
                #5. Ejecución y guardado de la consulta
                cursor.execute(sqlSelect)
                RSusuario = cursor.fetchall()
                conx.close()
                
                return RSusuario #guardar en una variable
                
            except sqlite3.OperationalError:
                print("Error Consulta")
        
        
    def ConsultarUsuario(self):
        conx = self.conexionBD()
        try:
            
            cursor = conx.cursor()
            sqlSelect= "select * from TBRegistrados"
            
            cursor.execute(sqlSelect)
            registros = cursor.fetchall()
            conx.close()
        
            return registros
    
        except sqlite3.OperationalError:
                print("Error Consulta")
    
        
    def actualizarUsuario():
        
        