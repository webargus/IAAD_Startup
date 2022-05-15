
"""
    Class ListFrame
    Authors: group UFRPE - BSI - IAAD - 2022
    Disclaimer: use it on your own risk!
    License: feel free to mess up with it at will, provided you display this header in your code!
"""

from tkinter import *
import tkinter.ttk as ttk
from TreeViewTable import *

class ListFrame():

    def __init__(self, frame):

        self.frame = frame
        self.table = None

    def listTable(self, columns):
        # destrói tabela anterior, se existir
        if(self.table is not None):
            self.table.destroy();
        
        # cria novo widget pra tabela
        self.table = TreeViewTable(self.frame, columns)






