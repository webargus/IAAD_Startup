

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
            print(error)
            self.console.insert_text("Erro: {}".format(error))
            self.popupOk(error)
            
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

    # def __del__ (self):
    #     self.cursor.close()
    #     self.conn.close()









