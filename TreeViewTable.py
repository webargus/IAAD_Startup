"""
    *************************************************************************
    *                                                                       *
    *   class TreeViewTable - herda de tkinter Treeview                     *
    *   simula tabela com cabeçalho e provê métodos para inserção/seleção   *
    *   de linhas                                                           *
    *                                                                       *
    *   ISENÇÃO DE RESPONSABILIDADE: o risco do uso é todo seu!             *
    *                                                                       *
    *   Autor: Grupo UFRPE - BSI - IAAD 2022.1                              *
    *                                                                       *
    *************************************************************************
"""


from tkinter import *
import tkinter.ttk as ttk


class TreeViewTable(ttk.Treeview):

    def __init__(self, frame, headers):
        super(TreeViewTable, self).__init__(frame, columns=headers, selectmode='browse')
        self.grid({"row": 0, "column": 0, "sticky": NSEW})  # sticky param needed for horz. + vert. treeview table stretching
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

        # inicializa event listener pra capturar seleção de linhas da TreeView
        self.callback_select = None
        self.bind('<<TreeviewSelect>>', self._handle_select)

    # adiciona linha à TreeView
    def appendItem(self, data, pos='', iid=None):
        self.insert(pos, 'end', iid, text=data[0], values=data[1:])

    # limpa TreeView
    def clear(self):
        self.delete(*self.get_children())

    # define callback que é chamada qdo ocorre seleção de linha
    def on_select(self, callback):
        self.callback_select = callback

    # chama callback de seleção de linha tendo como parâmetro a seleção
    def _handle_select(self, event):
        if self.callback_select is None:
            return
        self.callback_select(self.get_selection())

    # lê e retorna a linha selecionada
    def get_selection(self):
        selection = self.selection()
        ret = []
        for iid in selection:
            dict = self.item(iid)           # lê dados da seleção em dicionário
            dict.update({'iid': iid})       # acrescenta id (chave primária) da seleção
            ret.append(dict)
        return ret

