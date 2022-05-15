

import mysql.connector as connector
from sqlalchemy import false

class MySqlRepo:    
    
    def __init__(self, host = "localhost", username = "iaad", password = "123456", database="Startups"):

        try:
            
            self.conn = connector.connect(host=host,
                                          username= username,
                                          password= password,
                                          database = database)
            self.cursor = self.conn.cursor()
            
        except connector.Error as error:
            print (error)
            
        self.execute("USE `" + database + "`")

    def execute (self, query):
        
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except connector.Error as error:
            print (error)
            return false
    
    def __del__ (self):
        self.cursor.close()
        self.conn.close()









