
"""
    UFRPE - BSI - IAAD - 2ª VA
    Grupo: Edson + Joana + Christian + Douglas + J. Fernando
    Descrição: Interface gráfica para operações CRUD no BD Startups
"""

import sys
from tkinter import *
from tkinter.ttk import *
import Tools
from CRUDPanel import CRUDPanel
from ViewPanel import ViewPanel
from login import LoginDialog

class Gui(Frame):

    def __init__(self):
        
        # inicializa pai
        Frame.__init__(self)
        
        # centra janela na tela
        Tools.Tools.root(self.master)
        Tools.Tools.center_window(self.master, 1120, 600)
        # ícone UFRPE
        if ( sys.platform.startswith('win')): 
            self.master.iconbitmap('brasao32.ico')
        else:
            logo = PhotoImage(file='brasao.png')
            self.master.call('wm', 'iconphoto', self.master._w, logo)
        # config janela
        self.master.resizable(0, 0)
        self.master.state('normal')
        self.master.title("IAAD - Startups")
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.grid({"row": 0, "column": 0, "sticky": NSEW})
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # usando widget Notebook do tkinter pra criar abas
        self.notebook = Notebook(self)
        f1 = Frame(self.notebook)   # frame p/ CRUD
        f2 = Frame(self.notebook)   # frame p/ View
        
        # acrescenta abas
        self.notebook.add(f1, text='CRUD')
        self.notebook.add(f2, text='Views')
        self.notebook.grid({"row": 0, "column": 0, "sticky": NSEW})
        
        crudPanel = CRUDPanel(f1)
        self.viewPanel = ViewPanel(f2)
        
        # login
        dlg = LoginDialog(self)
        self.wait_window(dlg.top)
        
        # inicializa abas
        crudPanel.initCRUDPanel()
        self.viewPanel.initViewPanel()
        self.notebook.bind("<<NotebookTabChanged>>", self.handleTabChange)

        self.mainloop()
        
    # atualiza a aba view caso haja mudanças nas tabelas
    def handleTabChange(self, *args):
        if self.notebook.index(self.notebook.select()) == 1:
            self.viewPanel.initViewPanel()
        

if __name__ == '__main__':
    gui = Gui()









