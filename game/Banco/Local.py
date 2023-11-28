import psycopg2
from .Database import Database
from .Mundo import Mundo
from .Regiao import Regiao


class Local :
    def __init__(self):
        self.db = Database()
    pass
    
    def inserirLocal(self,coordenada, descrição,nome,tipo:bool,regiao):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Insert into local values({coordenada},'{descrição}','{nome}',{tipo},'{regiao}');""")
            insercaoMundo = conexao.commit()
            return print("Local inserido com sucesso")
        except psycopg2.Error as e:
            print("Erro ao inserir em Local", e)
        finally:
            cursor.close()
    
    def deletarLocal(self, coordenada):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""delete from local where coordenada = {coordenada};""")
            delecaoMundo = conexao.commit()
            return print("Local deletado com sucesso")
        except psycopg2.Error as e:
            print("Erro ao deletar em Local", e)
        finally:
            cursor.close()

    def consultarLocal(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"Select * from local;")
            consultaLocal = cursor.fetchall()
            for x in consultaLocal:
                print(x)
            return x
        except psycopg2.Error as e:
            print("Erro ao consultar local", e)
        finally:
            cursor.close()
    
    def consultarLocalCoordenada(self,coordena):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"Select * from local where coordenada = {coordena};")
            consultaLocal = cursor.fetchall()
            for x in consultaLocal:
                print(x)
            return x
        except psycopg2.Error as e:
            print("Erro ao consultar local", e)
        finally:
            cursor.close()
                
            