
"""
    Class ViewPanel
    Cria painel (frame) para listar as views do BD, bem como seus comandos de criação
    Autor: grupo UFRPE - BSI - IAAD - 2022
    ISENÇÃO DE RESPONSABILIDADE: o risco do uso é todo seu!
    Licença: use e/ou modifique o código à vontade, mas não apague esse cabeçalho.
"""

import imp
from tkinter import *
from tkinter.ttk import *
from MySqlRepo import *
from TreeViewTable import *
from ScrollableText import *
from ListFrame import *

class ViewPanel:
    
    def __init__(self, frame):

        frame.grid_rowconfigure(0, weight=0)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        
        # acrescenta console MySql (Frame F4)
        console_frame = Frame(frame)
        console_frame.grid({"row": 3, "column": 0, "pady": 8, "sticky": EW})
        console_frame.columnconfigure(0, weight=1)              # needed for stretching console horizontally
        self.console = ScrollableText(console_frame)
        
        # cria frame para listagem das views do BD (Frame F2)
        list_frame = Frame(frame)
        list_frame.grid({"row": 1, "column": 0, "sticky": NSEW}) # sticky NSEW needed for horz/vert table stretching
        list_frame.rowconfigure(0, weight=1)                     # needed for horz. + vert. treeview table stretching
        list_frame.columnconfigure(0, weight=1)                  # needed for horz. + vert. treeview table stretching
        # cria widget da listagem
        self.table = ListFrame(list_frame)
        
        # cria frame para exibir criação da view (Frame F3)
        view_frame = Frame(frame)
        view_frame.grid({"row": 2, "column": 0, "sticky": NSEW})
        view_frame.rowconfigure(0, weight=1)
        view_frame.columnconfigure(0, weight=1)
        # cria área de texto para exibir o comando de criação da view
        self.view_create = ScrollableText(view_frame)
        
        # cria frame no topo da GUI contendo combo com nomes das views (Frame F1)
        top_frame = Frame(frame)
        top_frame.grid({"row": 0, "column": 0})
        # rótulo para a combobox
        combo_label = Label(top_frame, text="Selecione a visão:")
        combo_label.grid({"row": 0, "column": 0})
        # cria combobox
        self.combo = Combobox(top_frame);
        self.combo.grid({"row": 0, "column": 1})
        # attach event listener -> lista tabela selecionada
        self.combo.bind("<<ComboboxSelected>>", lambda event: self.listTable(self.combo.get()))

    def initViewPanel(self):
        tables = MySqlRepo.repo.execute("SHOW FULL TABLES WHERE table_type = 'VIEW'", True)
        self.console.insert_text(tables["query"])
        if(tables["wasError"]):
            self.console.insert_text(tables["result"])
        else:
            tables = tables["result"]
            if len(tables) > 0:
                # lê nomes das VIEWS do BD
                tables = list((tables[x][0] for x in range(0, len(tables))))
                # insere nomes das views no combo
                self.combo["values"] = tables
                # seleciona a primeira VIEW e lista
                self.combo.set(tables[0])
                self.listTable(tables[0])
                
    def listTable(self, table_name):
        # mostra comando de criação da view
        self.showCreateView(table_name)
        
        # executa consulta pra pegar nomes das colunas da tabela
        res = MySqlRepo.repo.execute("DESCRIBE " + table_name, True)
        self.console.insert_text(res["query"])
        if(res["wasError"]):
            self.console.insert_text(res["result"])
        else:
            # pega só nomes das colunas do resultado da consulta
            res = res["result"]
            columns = list((res[ix][0] for ix in range(0,len(res))))
            # chama método para listar a tabela com os nomes das colunas
            self.table.listTable(table_name, columns)

    # mostra comando de criação da view
    def showCreateView(self, table_name):
        res = MySqlRepo.repo.execute("SHOW CREATE VIEW `{}`".format(table_name), True)
        self.console.insert_text(res["query"])
        if(res["wasError"]):
            self.console.insert_text(res["result"])
        else:
            # limpa área de texto
            self.view_create.clear()
            # copia comando de criação da view para a área de texto (F3)
            self.view_create.insert_text(res["result"][0][1])










