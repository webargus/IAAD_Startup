"""
    *************************************************************************
    *                                                                       *
    *   class TreeViewTable - inherits from tkinter Treeview                *
    *                                                                       *
    *   DISCLAIMER: Use it on your own risk!                                *
    *                                                                       *
    *************************************************************************
"""


from tkinter import *
import tkinter.ttk as ttk


class TreeViewTable(ttk.Treeview):

    def __init__(self, frame, headers):
        super(TreeViewTable, self).__init__(frame, columns=headers, selectmode='browse')
        self.grid({"row": 0, "column": 0, "sticky": NSEW})  # sticy param needed for horz. + vert. treeview table stretching
        self.rowconfigure(0, weight=1)                      # needed for horz. + vert. treeview table stretching
        self.columnconfigure(0, weight=1)                   # needed for horz. + vert. treeview table stretching
        #   acrescenta barra de rolagem
        tree_scroll = ttk.Scrollbar(frame, orient=VERTICAL, command=self.yview)
        tree_scroll.grid({"row": 0, "column": 1, "sticky": NS})
        self.configure(yscrollcommand=tree_scroll.set)
        # insere cabeçalhos e define suas larguras
        for ix, header in enumerate(headers):
            self.heading("#{}".format(ix), text=header, anchor=CENTER)
            self.column("#{}".format(ix), minwidth=100, width=150, stretch=NO, anchor=CENTER)

        self.callback_select = None
        self.bind('<<TreeviewSelect>>', self._handle_select)

    def appendItem(self, data, pos='', iid=None):
        self.insert(pos, 'end', None, text=data[0], values=data[1:])

    def clear(self):
        self.delete(*self.get_children())

    def on_select(self, callback):
        self.callback_select = callback

    def _handle_select(self, event):
        if self.callback_select is None:
            return
        self.callback_select(self.get_selection())

    def get_selection(self):
        selection = self.selection()
        ret = []
        for iid in selection:
            dict = self.item(iid)           # lê dados da seleção em dicionário
            dict.update({'iid': iid})       # acrescenta id (chave primária) da seleção
            ret.append(dict)
        return ret

    def clear_selection(self):
        for item in self.selection():
            self.selection_remove(item)

