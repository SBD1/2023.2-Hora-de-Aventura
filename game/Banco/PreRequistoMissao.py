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
    
    def consultarPreRequisitoNomeMissao(self, NomePreRequisito:str):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f""" select c1.requisitomissao,c2.descricao,c2.recompensa """
                           f""" from ( """
	                       f"""select p.requisitomissao  from prerequisitomissao p"""
	                       f""" left join missao on p.requisitomissao = missao.nome where p.nomeprerequisito = '{NomePreRequisito}' )as c1 """
                           f""" left join ( """
	                       f""" select missao.nome, missao.chefe , missao.descricao, missao.recompensa  from missao)as c2  """
                           f""" on c1.requisitomissao = c2.nome """)
            conexao.commit()
            resultado = cursor.fetchall()
            if resultado:
              return resultado
            else:
                print("Essa missão não possui pré-requisito")            
               
        except psycopg2.Error as e:
            print("Erro ao consultar PreRequisitoMissao", e)
        finally:
            cursor.close()
            