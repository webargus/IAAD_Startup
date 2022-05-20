
"""
    Class ListFrame
    Usa a classe TreeViewTable para listar as tabelas do BD
    Autor: grupo UFRPE - BSI - IAAD - 2022
    ISENÇÃO DE RESPONSABILIDADE: o risco do uso é todo seu!
    Licença: use e/ou modifique o código à vontade, mas não apague esse cabeçalho.
"""

from tkinter import *
from MySqlRepo import MySqlRepo
from tkinter import messagebox
from TreeViewTable import *

class ListFrame():

    def __init__(self, frame):

        self.frame = frame
        self.table = None

    def listTable(self, table_name, columns):
        # destrói tabela anterior, se existir
        if(self.table is not None):
            self.table.destroy()
        
        # cria novo treeview widget pra tabela
        self.table = TreeViewTable(self.frame, columns)
        
        # insere dados
        res = MySqlRepo.repo.execute("SELECT * FROM {}".format(table_name), True)
        if(res["wasError"]):
            messagebox.showwarning("...Êpa!!", ("Erro: {}\n Comando:{}\n".format(res["result"], res["query"])))
        else:
            for row in res["result"]:
                self.table.appendItem(row)

    # define callback pra chamar qdo seleciona linha da tabela
    def onRowSelect(self, callback):
        if(self.table is not None):
            self.table.on_select(callback)




