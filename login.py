
import sys
from tkinter import *
from tkinter import messagebox
from Tools import *
from MySqlRepo import *

class LoginDialog(Toplevel):

    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        # desabilita acesso à janela principal
        parent.grab_set()
        # ícone UFRPE
        if ( sys.platform.startswith('win')): 
            parent.master.iconbitmap('brasao32.ico')
        else:
            logo = PhotoImage(file='brasao.png')
            parent.master.call('wm', 'iconphoto', self.top._w, logo)
        # config diálogo e centra na tela
        self.parent = parent
        self.top.resizable(False, False)
        self.top.after(500, lambda: self.top.focus_force())
        self.top.transient(parent.master)
        self.top.protocol("WM_DELETE_WINDOW", self.__close)
        Tools.root(self.top)
        Tools.center_window(self.top, 400, 300)

        # cria frame para posicionar itens do formulário de login
        loginF = Frame(self.top)
        # loginF.grid(row=0, column=0, sticky="nsew")
        loginF.place({"relx": .5, "rely": .5, "anchor": CENTER})
        
        # cria cabeçalho do formulário
        Label(loginF, text="Entre suas credenciais:").grid({"row": 0, "column": 0, "columnspan": 2, "pady": 10})
        
        # cria rótulo para edit de entrada do nome do BD
        Label(loginF, {"text": "Banco de dados:"}).grid({"row": 1, "column": 0, "padx": 10, "pady": 10, "sticky": W})
        # cria edit de entrada do nome do BD
        database = Entry(loginF)
        database.grid({"row": 1, "column": 1, "padx": 10, "pady": 10})
        
        # cria rótulo para edit de entrada do nome do usuário
        Label(loginF, {"text": "Nome de usuário:"}).grid({"row": 2, "column": 0, "padx": 10, "pady": 10, "sticky": W})
        # cria edit para entrada do nome do usuário
        login = Entry(loginF)
        login.grid({"row": 2, "column": 1, "padx": 10, "pady": 10})
        
        # cria rótulo para edit de entrada da senha
        Label(loginF, {"text": "Senha:"}).grid({"row": 3, "column": 0, "padx": 10, "pady": 10, "sticky": W})
        # cria edit para entrada da senha
        pwd = Entry(loginF, {"show": "*"})
        pwd.grid({"row": 3, "column": 1, "padx": 10, "pady": 10})
        
        Button(loginF,
               {"text": "Conectar", "width": 10,
                "command": lambda: self.__login(database.get(), login.get(), pwd.get())}).grid(
                    {"row": 4, "column": 0, "columnspan": 2, "pady": 10})


    def __login(self, database, username, password):
        # tenta conectar
        ret = MySqlRepo()
        ret = ret.connect(username=username, password=password, database=database)
        if ret["wasError"]:
            # exibe erro em popup
            self.popupOk(ret["result"])
            return
            
        # habilita janela principal
        self.top.grab_release()
        self.top.destroy()

    def __close(self):
        self.top.destroy()
        self.parent.master.destroy()

    def popupOk(self, error):
        box = messagebox.showwarning("...Êpa!!", ("Favor verificar:\n{}".format(error)), parent=self.top)
