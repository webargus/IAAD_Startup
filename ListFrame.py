
"""
    Class ListFrame
    Authors: group UFRPE - BSI - IAAD - 2022
    Disclaimer: use it on your own risk!
    License: feel free to mess up with it at will, provided you display this header in your code!
"""

from tkinter import *
from TreeViewTable import *

class ListFrame():

    def __init__(self, frame, repo):

        self.frame = frame
        self.repo = repo
        self.table = None

    def listTable(self, table_name, columns):
        # destrói tabela anterior, se existir
        if(self.table is not None):
            self.table.destroy()
        
        # cria novo treeview widget pra tabela
        self.table = TreeViewTable(self.frame, columns)
        
        # insere dados
        res = self.repo.execute("SELECT * FROM {}".format(table_name))
        if(res):
            for row in res:
                self.table.appendItem(row, iid=row[0])






