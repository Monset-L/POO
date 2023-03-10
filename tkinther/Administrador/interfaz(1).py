from tkinter import Tk, Button, Frame,Label,Entry


def int1 ():
    login=Tk ()

    login.title("Caja Popular")
    login.geometry("500x450")

    seccion1=Frame(login,bg="#9BC1BC")
    seccion1.pack(expand=True,fill='both')

    titulo = Label(text="Consultar saldo",fg="Black",font=('Times',30),bg="#9BC1BC")
    titulo.place(x=140,y=20)
        
    Label(text="No. Cuenta",font="30").place(x=70, y=150)
    Cuenta= Entry(login,font="20").place(x=220, y=150)

    Label(text="Titular",font="30").place(x=70, y=200)
    Titular= Entry(login,font="20").place(x=220, y=200)

    boton= Button(seccion1,text="Ingresar",fg="black",bg="#F4F1BB",font=(10))
    boton.place(x=220,y=260)
    
    login.mainloop()
    
    
    
def int2 ():
    Ingresar=Tk ()

    Ingresar.title("Caja Popular")
    Ingresar.geometry("500x450")

    seccion1=Frame(Ingresar,bg="#9BC1BC")
    seccion1.pack(expand=True,fill='both')

    titulo = Label(text="Consultar saldo",fg="Black",font=('Times',30),bg="#9BC1BC")
    titulo.place(x=140,y=20)
        
    Label(text="No. Cuenta",font="30").place(x=70, y=150)
    Cuenta= Entry(Ingresar,font="20").place(x=220, y=150)

    Label(text="Titular",font="30").place(x=70, y=200)
    Titular= Entry(Ingresar,font="20").place(x=220, y=200)

    boton2= Button(seccion1,text="Ingresar",fg="black",bg="#F4F1BB",font=(10))
    boton2.place(x=220,y=260)

    Ingresar.mainloop()