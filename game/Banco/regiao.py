import psycopg2
from database import Database
class regiao:
    def __init__(self):
        self.db = Database()
    
    def inserirRegiao(self,nome, mundo):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f""" insert into regiao values('{nome}','{mundo}');""")
            insercaoRegiao = conexao.commit()
            return print("Região inserida com sucesso")
        except psycopg2.Error as e:
            print("Erro ao inserir em Mundo", e)
        finally:
            cursor.close()
    
    def deletarRegiao(self, nome):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""delete from regiao where nome = '{nome}';""")
            delecaoRegiao = conexao.commit()
            return print("Regiao deletado com sucesso")
        except psycopg2.Error as e:
            print("Erro ao deletar em Regiao", e)
        finally:
            cursor.close()    
                              
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

    def consultarRegiaoNome(self,nome):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Select * from regiao where nome = '{nome}';""")
            consultarRegiao = cursor.fetchall()
            for x in consultarRegiao:
                print(x)
            return x
        except psycopg2.Error as e:
            print("Erro ao consultar ")
        finally:
            cursor.close()

                  
        
            