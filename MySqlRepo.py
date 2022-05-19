
"""
    *************************************************************************
    *                                                                       *
    *   class MySqlRepo                                                     *
    *   provê conexão com BD usando o conector MySql pra Python que deve já *
    *   estar instalado na máquina do aplicativo que for usar a conexão     *
    *   download: https://dev.mysql.com/downloads/connector/python/         *
    *                                                                       *
    *   ISENÇÃO DE RESPONSABILIDADE: o risco do uso é todo seu!             *
    *                                                                       *
    *   Autor: Grupo UFRPE - BSI - IAAD 2022.1                              *
    *                                                                       *
    *************************************************************************
"""

import mysql.connector as connector
from tkinter import messagebox

    
class MySqlRepo:    
    
    def __init__(self, console, host = "localhost", username = "iaad", password = "123456", database="Startups"):

        try:
            # linka console da GUI com a saída do método execute
            self.console = console
            # tenta conectar ao BD
            self.conn = connector.connect(host=host,
                                          user= username,
                                          passwd= password,
                                          database = database)
            # define cursor MySql para comandos/consultas
            self.cursor = self.conn.cursor()
            
        except connector.Error as error:
            # imprime erro no console da IDE
            print(error)
            # apresenta erro na GUI
            self.console.insert_text("Erro: {}".format(error))
            # exibe erro em popup antes de abortar caso tenha havido falha na conexão com o BD
            self.popupOk(error)
            
        # seleciona o BD pra usar no programa
        self.execute("USE `" + database + "`")

    def execute (self, query):
        
        try:
            self.console.insert_text("Comando: " + query)
            self.cursor.execute(query)
            # self.conn.commit()
            return self.cursor.fetchall()
        except connector.Error as error:
            self.console.insert_text("Erro: {}".format(error))
            return False
    
    def popupOk(self, error):
        msg = "Favor verificar:\n"
        messagebox.showwarning("...Êpa!!", (msg + "\n{}".format(error)))

    def __del__ (self):
        self.cursor.close()
        self.conn.close()









