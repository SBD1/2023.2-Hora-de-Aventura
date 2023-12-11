import psycopg2
from .Database import Database

class Chefe:
    def __init__(self):
        self.db=Database()

    def inserirChefe(self, Numero:int, nomeMissao:str, Personagem:int):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""INSERT INTO Chefe VALUES({Numero}, '{nomeMissao}', {Personagem});""")
            conexao.commit()
            return print("Chefe Inserido")
        except psycopg2.Error as e:
            print("Erro ao inserir Chefe", e)
        finally:
            cursor.close()

    def consultarChefe(self):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT * FROM Chefe;""")
            conexao.commit()
            resultado=cursor.fetchall()
            for i in resultado:
                print(i)
        except psycopg2.Error as e:
            print("Erro ao consultar Chefe", e)
        finally:
            cursor.close()

    def deletarChefe(self, Numero:int, nomeMissao:str, Personagem:int):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""DELETE FROM Chefe WHERE Numero = {Numero} AND nomeMissao = '{nomeMissao}' AND Personagem = {Personagem};""")
            conexao.commit()
            return print("Chefe Deletado")
        except psycopg2.Error as e:
            print("Erro ao deletar Chefe", e)
        finally:
            cursor.close()

    def consultarChefeEspecifico(self, Numero:int, nomeMissao:str, Personagem:int):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT * FROM Chefe WHERE Numero = {Numero} AND nomeMissao = '{nomeMissao}' AND Personagem = {Personagem};""")
            conexao.commit()
            resultado=cursor.fetchall()
            if resultado:
                print(resultado[0])
        except psycopg2.Error as e:
            print("Erro ao consultar Chefe", e)
        finally:
            cursor.close()