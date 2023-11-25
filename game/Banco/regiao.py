import psycopg2
from database import Database


class regiao:
    def __init__(self):
        self.db = Database()
    
    
    def consultarRegiao(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Select * from regiao;""")
            consultarRegiao = cursor.fetchall()
            for x in consultarRegiao:
                print(x)
            return x
        except psycopg2.Error as e:
            print("Erro ao consultar ")
        finally:
            cursor.close()

                
        
            