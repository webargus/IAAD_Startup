
"""
    UFRPE - BSI - IAAD - 2ª VA
    Descrição: Interface gráfica para operações CRUD no BD Startups
"""

from textwrap import fill
from tkinter import *
from tkinter.ttk import *
from MySqlRepo import *
from ScrollableText import *
import Tools


class Gui(Frame):

    def __init__(self):
        
        Frame.__init__(self)
        Tools.Tools.root(self.master)
        Tools.Tools.center_window(self.master, 1120, 600)
        # self.master.iconbitmap("brasao32.ico")
        self.master.resizable(0, 0)
        self.master.state('normal')
        self.master.title("IAAD - Startups")
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.grid({"row": 0, "column": 0, "sticky": NSEW})
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # acrescenta console MySql (Frame F4)
        console_frame = Frame(self)
        console_frame.grid({"row": 1, "column": 0, "pady": 8})
        self.console = ScrollableText(console_frame)
        
        # cria repositório MySql linkado com o console
        repo = MySqlRepo(self.console)
        
        top_frame = Frame(self)
        top_frame.grid({"row": 0, "column": 0})
        # top_frame.pack(padx=8, pady=8)

        combo_label = Label(top_frame, text="Selecione a tabela:")
        combo_label.grid({"row": 0, "column": 0})
        
        combo = Combobox(top_frame, values = repo.execute("SHOW TABLES"));
        combo.grid({"row": 0, "column": 1})
        
        self.mainloop()

if __name__ == '__main__':
    gui = Gui()






