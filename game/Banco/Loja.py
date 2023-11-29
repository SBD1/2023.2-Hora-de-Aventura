import psycopg2
from .Database import Database

class Loja:
    def __init__(self):
        self.db=Database()

    def inserirLoja(self, Nome:str, Tipo:str, Dano:int, Elemento:str, Local:int):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""INSERT INTO Loja VALUES('{Nome}', '{Tipo}',{Dano}, '{Elemento}', {Local});""")
            conexao.commit()
            return print("Loja Inserida")
        except psycopg2.Error as e:
            print("Erro ao inserir Loja", e)
        finally:
            cursor.close()

    def consultarLoja(self):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT * FROM Loja;""")
            conexao.commit()
            resultado=cursor.fetchall()
            for i in resultado:
                print(i)
        except psycopg2.Error as e:
            print("Erro ao consultar Loja", e)
        finally:
            cursor.close()

    def deletarLoja(self, Nome:str, Tipo:str):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""DELETE FROM Loja WHERE Nome = '{Nome}' AND Tipo = '{Tipo}';""")
            conexao.commit()
            return print("Loja Deletada")
        except psycopg2.Error as e:
            print("Erro ao deletar Loja", e)
        finally:
            cursor.close()

    def consultarLojaEspecifico(self, Nome:str, Tipo:str):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT * FROM Loja WHERE Nome = '{Nome}' AND Tipo = '{Tipo}';""")
            conexao.commit()
            resultado=cursor.fetchall()
            if resultado:
                print(resultado[0])
        except psycopg2.Error as e:
            print("Erro ao consultar Loja", e)
        finally:
            cursor.close()

