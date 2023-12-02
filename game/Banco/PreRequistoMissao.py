import psycopg2
from .Database import Database

class PreRequisitoMissao:
    def __init__(self):
        self.db=Database()

    def inserirPreRequisitoMissao(self, NomePreRequisito:str, RequisitoMissao:str):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""INSERT INTO PreRequisitoMissao VALUES('{NomePreRequisito}', '{RequisitoMissao}');""")
            conexao.commit()
            return print("PreRequisitoMissao Inserido")
        except psycopg2.Error as e:
            print("Erro ao inserir PreRequisitoMissao", e)
        finally:
            cursor.close()

    def consultarPreRequisitoMissao(self):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT * FROM PreRequisitoMissao;""")
            conexao.commit()
            resultado=cursor.fetchall()
            for i in resultado:
                print(i)
        except psycopg2.Error as e:
            print("Erro ao consultar PreRequisitoMissao", e)
        finally:
            cursor.close()
    
    def deletarPreRequisitoMissao(self, NomePreRequisito:str, missao:str):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""DELETE FROM PreRequisitoMissao WHERE NomePreRequisito = '{NomePreRequisito}' AND RequisitoMissao = '{missao}';""")
            conexao.commit()
            return print("PreRequisitoMissao Deletada")
        except psycopg2.Error as e:
            print("Erro ao deletar PreRequisitoMissao", e)
        finally:
            cursor.close()
    
    def consultarPreRequisitoMissaoEspecifico(self, NomePreRequisito:str, RequisitoMissao:str):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT * FROM PreRequisitoMissao WHERE NomePreRequisito = '{NomePreRequisito}' AND RequisitoMissao = '{RequisitoMissao}';""")
            conexao.commit()
            resultado=cursor.fetchall()
            if resultado:
                print(resultado[0])
        except psycopg2.Error as e:
            print("Erro ao consultar PreRequisitoMissao", e)
        finally:
            cursor.close()