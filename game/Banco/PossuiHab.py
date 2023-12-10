import psycopg2
from .Database import Database
from .Habilidade import Habilidade
from .Personagem import Personagem

class PossuiHab:
    def __init__(self):
        self.db = Database()
    pass

    def inserirPossuiHab(self, personagem:int, habilidade:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Insert into possuihab values({personagem},{habilidade});""")
            inserirDropItem = conexao.commit()
        except psycopg2.IntegrityError as e:
            print(f"Erro ao inserir possuihab", e)
        finally:
            cursor.close()
    
    def inserirPossuiHabIncremento(self,habilidade:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""INSERT INTO possuihab VALUES((SELECT COALESCE(MAX(personagem), 0) FROM pc),{habilidade})""")
            inserirDropItem = conexao.commit()
        except psycopg2.IntegrityError as e:
            print(f"Erro ao inserir possuihab", e)
        finally:
            cursor.close()

    def consultarPossuiHabPK(self,personagem:int, habilidade:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM possuihab WHERE personagem = {personagem} and habilidade = {habilidade};")
            consulta = cursor.fetchall()

            if not consulta:
                print("Não foi há possuiHab cadastrados\n")
            else:
                return consulta
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")
        finally:
            cursor.close()

    def getPossuiHabPK(self,personagem: int, idescolhido: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT IDhabilidade, Nome, Tempo_de_recarga, Dano "
                           f"FROM Habilidade "
                           f"INNER JOIN PossuiHab ON Habilidade = IDhabilidade "
                           f"WHERE Personagem = {personagem} AND idhabilidade = {idescolhido};")
            consulta = cursor.fetchall()
            if consulta:
                return consulta
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")
        finally:
            cursor.close()
    
    def consultarPossuiHab(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM possuiHab ;")
            consulta = cursor.fetchall()

            if not consulta:
                print("Não foi há itens cadastrados\n")
            else:
                return consulta
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")
        finally:
            cursor.close()
            
    def deletarPossuiHabilidade(self, personagem:int, habilidade:int):
        try:
            conexao = self.db.conexao
            cursor =  conexao.cursor()
            cursor.execute(f"DELETE FROM possuihab WHERE personagem = {personagem} and habilidade = {habilidade};")
            delecaoFazMissao = conexao.commit()
            return print("PossuiHab  deletado com sucesso!\n")

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a delecao. Erro: {e}\n")
        
        finally:
            cursor.close()

    def deletarPossuiHabALL(self, personagem: int):
        try:
            conexao = self.db.conexao
            cursor =  conexao.cursor()
            cursor.execute(f"DELETE FROM possuihab WHERE personagem = {personagem};")
            delecaoFazMissao = conexao.commit()
            return 

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a delecao. Erro: {e}\n")
        
        finally:
            cursor.close()


    def consultarPossuiHabPersonagem(self,nome:str):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT IDhabilidade, Nome, Tempo_de_recarga, Dano "
                           f"FROM Habilidade "
                           f"INNER JOIN PossuiHab ON Habilidade = IDhabilidade "
                           f"WHERE Personagem = '{nome}';")
            consulta = cursor.fetchall()
            if not consulta:
                print("Não foi há possuiHab cadastrados\n")
            else:
                return consulta
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")
        finally:
            cursor.close()
   
        