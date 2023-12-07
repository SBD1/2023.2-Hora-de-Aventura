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

    def getLojaLocal(self, Local: int):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT * FROM loja WHERE local = '{Local}';""")
            conexao.commit()
            resultado = cursor.fetchall()
            if resultado:
                print("\033[1;32mLoja Disponível!\033[0m")
                for lojaAtributo in resultado:
                    nome = lojaAtributo[0].strip()
                    tipo = lojaAtributo[1].strip()
                    print(f"Nome = {nome}, Tipo = {tipo}")
                return resultado
        except psycopg2.IntegrytError as e:
            print("Erro ao consultar Loja", e)
        finally:
            cursor.close()

