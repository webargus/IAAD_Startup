
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


class Gui(Frame):

    def __init__(self):
        
        Frame.__init__(self)
        Tools.Tools.root(self.master)
        Tools.Tools.center_window(self.master, 1120, 600)
        if ( sys.platform.startswith('win')): 
            self.master.iconbitmap('brasao32.ico')
        else:
            logo = PhotoImage(file='brasao.png')
            self.master.call('wm', 'iconphoto', self.master._w, logo)
        self.master.resizable(0, 0)
        self.master.state('normal')
        self.master.title("IAAD - Startups")
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.grid({"row": 0, "column": 0, "sticky": NSEW})
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        n = Notebook(self)
        f1 = Frame(n)   # frame p/ CRUD
        f2 = Frame(n)   # frame p/ View
        
        #   acrescenta abas
        n.add(f1, text='CRUD')
        n.add(f2, text='Views')
        n.grid({"row": 0, "column": 0, "sticky": NSEW})
        
        CRUDPanel(f1)
        ViewPanel(f2)

        self.mainloop()

if __name__ == '__main__':
    gui = Gui()









