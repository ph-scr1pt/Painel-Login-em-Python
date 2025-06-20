#============Importar Biblioteca============#
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser


#============Criar Janela============#
janela = Tk()

janela.title("DP Systems - Acess Panel")
janela.geometry("600x300")
janela.configure(background="white")
janela.resizable(width=False, height=False) #bloqueia a movimentação das propriedades do tamanho
janela.attributes("-alpha", 0.9) #transparência
janela.iconbitmap(default="D:\Programação\Login\icons\icone.ico")


#============Carregar Imagem============#
logo = PhotoImage(file="D:\Programação\Login\icons\logo.png")

#============Limitar Caracteres============#
def Check(new_text):
    return len(new_text) <= 8 and (new_text.isalnum() or new_text == "")



vcmd = (janela.register(Check), '%P')


#============Widgets da Janela============#
LeftFrame = Frame(janela, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

Rightframe = Frame(janela, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
Rightframe.pack(side=RIGHT)

#============Logo do painel============#
LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=30, y=80)

#============Parte do Username============#
UserLabel = Label(Rightframe, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(Rightframe, width=30, validate="key", validatecommand=vcmd)
UserEntry.place(x=150, y=111)

#============Parte da Senha============#
PassLabel = Label(Rightframe, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x=6, y=140)

PassEntry = ttk.Entry(Rightframe, width=30, show="•", validate="key", validatecommand=vcmd)
PassEntry.place(x=150, y=150)

def Login():
    Pass = PassEntry.get()
    User = UserEntry.get()

    DataBaser.cursor.execute("""
        SELECT * FROM Users
        WHERE User = ? AND Password = ?
    """, (User, Pass))
    print('selected')
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if(User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login info", message="Access Granted. Welcome!")
    except:
            messagebox.showinfo(title="Login info", message="Acesso Denied. Check if you are registered in the system.")
        
#============Botões============#
LoginButton = ttk.Button(Rightframe, text="Login", width=25, command = Login)
LoginButton.place(x=160, y=200)


def Register():
    #Removendo widgets de Login
    LoginButton.place(x=999)
    RegisterButton.place(x=999)
    #Inserindo widgets de Registro
    NomeLabel = Label(Rightframe, text="Name:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=5, y=20)

    NomeEntry = ttk.Entry(Rightframe, width=30)
    NomeEntry.place(x=100, y=30)

    EmailLabel = Label(Rightframe, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=5, y=60)

    EmailEntry = ttk.Entry(Rightframe, width=30)
    EmailEntry.place(x=100, y=71)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Register Error", message="Check if all filds are filled.")
        else:

            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES (?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register info", message="Account created sucessfully")

    Register = ttk.Button(Rightframe, text="Register", width=25, command=RegisterToDataBase)
    Register.place(x=160, y=200)

    def BackToLogin():
        #Removendo widget de Registro
        NomeLabel.place(x=999)
        NomeEntry.place(x=999)
        EmailEntry.place(x=999)
        EmailLabel.place(x=999)
        Register.place(x=999)
        Back.place(x=999)
        LoginButton.place(x=160, y=200)
        RegisterButton.place(x=160, y=235)

    Back = ttk.Button(Rightframe, text="Back", width=25, command=BackToLogin)
    Back.place(x=160, y=235)

RegisterButton = ttk.Button(Rightframe, text="Register", width=25, command=Register)
RegisterButton.place(x=160, y=235)




janela.mainloop()