
"""
    UFRPE - BSI - IAAD - 2ª VA
    Grupo: Edson + Joana + Christian + Douglas + J. Fernando
    Descrição: Interface gráfica para operações CRUD no BD Startups
"""

from textwrap import fill
from tkinter import *
from tkinter.ttk import *
from MySqlRepo import *
from ScrollableText import *
from ListFrame import *
from FormFrame import *
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
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.grid({"row": 0, "column": 0, "sticky": NSEW})      # needed for stretching console horizontally
        self.columnconfigure(0, weight=1)                       # needed for stretching console horizontally
        self.rowconfigure(0, weight=1)                
        self.rowconfigure(1, weight=10)
        self.rowconfigure(2, weight=1)
        
        # acrescenta console MySql (Frame F4)
        console_frame = Frame(self)
        console_frame.grid({"row": 3, "column": 0, "pady": 8, "sticky": EW})
        console_frame.columnconfigure(0, weight=1)              # needed for stretching console horizontally
        self.console = ScrollableText(console_frame)
        # cria repositório MySql linkado com o console
        self.repo = MySqlRepo(self.console)
        
        # cria frame para listagem das tabelas do BD (Frame F2)
        list_frame = Frame(self)
        list_frame.grid({"row": 1, "column": 0, "sticky": NSEW}) # sticky NSEW needed for horz/vert table stretching
        list_frame.rowconfigure(0, weight=1)                     # needed for horz. + vert. treeview table stretching
        list_frame.columnconfigure(0, weight=1)                  # needed for horz. + vert. treeview table stretching
        # cria widget da listagem
        self.table = ListFrame(list_frame, self.repo)
        
        # cria frame para formulário de edição C.U.D. (Frame F3)
        form_frame = Frame(self)
        form_frame.grid({"row": 2, "column": 0, "sticky": NSEW})
        form_frame.rowconfigure(0, weight=1)
        form_frame.columnconfigure(0, weight=1)
        self.form = FormFrame(form_frame, self.repo)
        
        # cria frame no topo da GUI contendo combo com nomes das tabelas (Frame F1)
        top_frame = Frame(self)
        top_frame.grid({"row": 0, "column": 0})
        # rótulo para a combobox
        combo_label = Label(top_frame, text="Selecione a tabela:")
        combo_label.grid({"row": 0, "column": 0})
        # cria combo
        tables = self.repo.execute("SHOW TABLES")
        if(tables):          # lê nomes das tabelas do BD
            combo = Combobox(top_frame, values = tables);
            combo.grid({"row": 0, "column": 1})
            # attach event listener -> lista tabela selecionada
            combo.bind("<<ComboboxSelected>>", lambda event: self.listTable(combo.get()))
            # seleciona a primeira tabela e lista
            combo.set(tables[0][0])
            self.listTable(tables[0][0])
        
        self.mainloop()
        
    def listTable(self, table_name):
        # executa consulta pra pegar nomes das colunas da tabela
        res = self.repo.execute("DESCRIBE " + table_name)
        if(res):
            # pega só nomes das colunas do resultado da consulta
            columns = list((res[ix][0] for ix in range(0,len(res))))
            # chama método para listar a tabela com os nomes das colunas
            self.table.listTable(table_name, columns)
            # attach event listener for table row selection
            self.table.onRowSelect(self.handleRowSelect)

            # prepara formulário para operações CRUD com a tabela listada
            self.form.setForm(table_name, columns)
            
    def handleRowSelect(self, selection):
        # transfere texto-âncora da treeview (== id da entrada na tabela) para a lista de valores da linha
        values = selection[0]["values"]
        values.insert(0, selection[0]["text"])
        # transfere linha selecionada para F3 (== formulário CRUD)
        self.form.setFormValues(values)

if __name__ == '__main__':
    gui = Gui()









