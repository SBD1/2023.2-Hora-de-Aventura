import psycopg2
from .Database import Database


class Mundo: 
    def __init__(self):    
        self.db = Database()
    pass 

    def inserirMundo(self,nome:str,mundoDestino:str):
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
    
    def deletarMundo(self, nome:str):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""delete from mundo where nome = '{nome}';""")
            delecaoMundo = conexao.commit()
            return print("Mundo deletado com sucesso")
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
            
    def consultarMundoNome(self,nome:str):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Select * from mundo where nome = '{nome}';""")
            consulta = cursor.fetchall()
            for x in consulta:
                print(x)
        except psycopg2.Error as e:
            print("Erro ao executar a consulta:", e)
        finally:
            cursor.close()
