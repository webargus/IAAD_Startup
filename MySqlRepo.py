

import mysql.connector as connector

class MySqlRepo:    
    
    def __init__(self, console, host = "localhost", username = "iaad", password = "123456", database="Startups"):

        try:
            # linka console da GUI com a saída do método execute
            self.console = console
            # tenta conectar ao BD
            self.conn = connector.connect(host=host,
                                          username= username,
                                          password= password,
                                          database = database)
            # define cursor MySql para comandos/consultas
            self.cursor = self.conn.cursor()
            
        except connector.Error as error:
            self.conn.append_text("Erro: " + error)
            
        self.execute("USE `" + database + "`")

    def execute (self, query):
        
        try:
            self.console.append_text("Comando: " + query)
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except connector.Error as error:
            self.console.append_text("Erro: " + query)
            return False
    
    # def __del__ (self):
    #     self.cursor.close()
    #     self.conn.close()









