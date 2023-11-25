import psycopg2
from database import Database


class mundo:
    ## construtor com argumento  
    def __init__(self, nome, mundoDestino):
        self.nome = nome 
        self.mundoDestino = mundoDestino
    pass
    ## construtor sem nada 
    def __init__(self):    
        self.db = Database()
    pass 

    def consultarMundo(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Select * from mundo;""")
            consulta = cursor.fetchall()
            consultas = []
            for x in consulta:
                consultas.append(x)
            for resultado in consultas:
                print(resultado)
            return resultado    
        except psycopg2.Error as e:
            print("Erro ao executar a consulta:", e)
        finally:
            cursor.close()
  
Mundo = mundo()  
Mundo.consultarMundo()            

