

import mysql.connector as connector

conn = connector.connect(
    host="localhost",
    username="iaad",
    password="123456",
    database="Startups"
)

cursor = conn.cursor()
try:
    cursor.execute("SELECT mm FROM `Startup`")
    for data in cursor:
        print (data)

except connector.Error as error:
    print (error)













