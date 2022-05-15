
"""
    Class ListFrame
    Authors: group UFRPE - BSI - IAAD - 2022
    Disclaimer: use it on your own risk!
    License: feel free to mess up with it at will, provided you display this header in your code!
"""

from tkinter import *
import tkinter.ttk as ttk


class ListFrame(ttk.Treeview):

    def __init__(self, frame):

        super(ListFrame, self).__init__(frame)

    def listTable(self, columns):
        
        for column in columns:
            print(column)

