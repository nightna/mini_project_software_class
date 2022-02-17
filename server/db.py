import mysql.connector

class DB:
    def __init__(self, host, user, db, password):
        self.host = host
        self.user = user
        self.db = db
        self.password = password
    
    def connect(self):
        return mysql.connector.connect(host=self.host , user = self.user, password = self.password, db = self.db )
    
    def insert_or_update(self, sql, value):
        mydb = self.connect()
        mycursor = mydb.cursor(dictionary = True)
        mycursor.execute(sql, value)
        mydb.commit()
    
    def select(self, sql):
        mydb = self.connect()
        mycursor = mydb.cursor(dictionary = True)
        mycursor.execute(sql)
        return mycursor.fetchall()