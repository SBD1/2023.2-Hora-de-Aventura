import psycopg2
from Database import Database

class Missao:
    def __init__(self):
        self.db=Database()
    
    def inserirMissao(self, nome:str, chefe:bool, descricao:str, recompensa:int):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""INSERT INTO Missao VALUES('{nome}', {chefe}, '{descricao}', {recompensa});""")
            conexao.commit()
            return print("Missão Inserida")
        except psycopg2.Error as e:
            print("Erro ao inserir Missão", e)
        finally:
            cursor.close()

    def consultarMissao(self):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT * FROM Missao;""")
            conexao.commit()
            resultado=cursor.fetchall()
            for i in resultado:
                print(i)
        except psycopg2.Error as e:
            print("Erro ao consultar Missão", e)
        finally:
            cursor.close()      

    def deletarMissao(self, nome:str):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""DELETE FROM Missao WHERE NOME = '{nome}';""")
            conexao.commit()
            return print("Missão Deletada")
        except psycopg2.Error as e:
            print("Erro ao deletar Missão", e)
        finally:
            cursor.close()

    def consultarMissaoNome(self, nome:str):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT * FROM Missao WHERE NOME = '{nome}';""")
            conexao.commit()
            resultado=cursor.fetchall()
            if resultado:
                print(resultado[0])
        except psycopg2.Error as e:
            print("Erro ao consultar Missão", e)
        finally:
            cursor.close() 
