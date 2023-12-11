import psycopg2

class Database:
    def __init__(self):
        self.conexao = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres123")
        pass  
    
   