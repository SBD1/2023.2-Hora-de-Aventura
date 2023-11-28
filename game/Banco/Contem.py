import psycopg2
from Database import Database

class Contem:
    def __init__(self):
        self.db=Database()

    def inserirContem(self, local:int, missao:str, status:bool):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""INSERT INTO Contem VALUES({local}, '{missao}', {status});""")
            conexao.commit()
            return print("Contem Inserido")
        except psycopg2.Error as e:
            print("Erro ao inserir Contem", e)
        finally:
            cursor.close()

    def consultarContem(self):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT * FROM Contem;""")
            conexao.commit()
            resultado=cursor.fetchall()
            for i in resultado:
                print(i)
        except psycopg2.Error as e:
            print("Erro ao consultar Contem", e)
        finally:
            cursor.close()
    
    def deletarContem(self, local:int, missao:str):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""DELETE FROM Contem WHERE LOCAL = '{local}' AND MISSAO = '{missao}';""")
            conexao.commit()
            return print("Contem Deletada")
        except psycopg2.Error as e:
            print("Erro ao deletar Contem", e)
        finally:
            cursor.close()
    
    def consultarContemEspecifico(self, local:int, missao:str):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT * FROM Contem WHERE LOCAL = '{local}' AND MISSAO = '{missao}';""")
            conexao.commit()
            resultado=cursor.fetchall()
            if resultado:
                print(resultado[0])
        except psycopg2.Error as e:
            print("Erro ao consultar Contem", e)
        finally:
            cursor.close()