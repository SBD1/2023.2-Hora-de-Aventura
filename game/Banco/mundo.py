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

    def inserirMundo(self,nome,mundoDestino):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Insert into mundo values('{nome}','{mundoDestino}');""")
            insercaoMundo = conexao.commit()
            return print("Mundo inserido com sucesso")
        except psycopg2.Error as e:
            print("Erro ao inserir em Mundo", e)
        finally:
            cursor.close()
    
    def deletarMundo(self, nome):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""delete from mundo where nome = '{nome}';""")
            delecaoMundo = conexao.commit()
            return True
        except psycopg2.Error as e:
            print("Erro ao deletar em Mundo", e)
        finally:
            cursor.close()    
    def consultarMundo(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Select * from mundo;""")
            consulta = cursor.fetchall()
            for x in consulta:
                print(x)
            return x
        except psycopg2.Error as e:
            print("Erro ao executar a consulta:", e)
        finally:
            cursor.close()
    
