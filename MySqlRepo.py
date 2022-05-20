
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
    
class MySqlRepo:    
    
    repo = None
        
    # conecta com BD
    def connect (self, host = "localhost", username = "iaad", password = "123456", database="Startups"):
        self.conn = self.cursor = None
        try:
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
            return {"wasError": True, "query": "", "result": "Erro: {}".format(error)}

        # conexão deu certo -> define (static) global para uso no programa
        MySqlRepo.repo = self
        
        # seleciona o BD pra usar no programa
        return self.execute("USE `" + database + "`")
       
        
    # executa comando/consulta
    def execute (self, query):
        
        try:
            self.cursor.execute(query)
            # retorna dicionário com resultado se a consulta/comando teve sucesso
            return {"wasError": False, "query": "Comando: {}".format(query), "result": self.cursor.fetchall()}
        except connector.Error as error:
            # retorna dicionário com descrição do erro se a consulta/comando falhou
            return {"wasError": True, "query": "Comando: {}".format(query), "result": "Erro: {}".format(error)}

    # fecha cursor e conexão antes de o garbage collector deletar o obj
    def __del__ (self):
        if self.conn is not None:
            self.cursor.close()
            self.conn.close()









