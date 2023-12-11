import psycopg2
from .Database import Database
from .Npc import Npc
from .Item import Item


class Dropa:
    def __init__(self):
        self.db = Database()
    pass

    def inserirDropDeItem(self, Npc:int, numeroItem:int, IDItem:int, chance:float):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Insert into dropa values({Npc},{numeroItem},{IDItem},{chance});""")
            inserirDropItem = conexao.commit()
            return print("Drop de item inserido com sucesso")

        except psycopg2.IntegrityError as e:
            print(f"Erro ao inserir Drop de item", e)
        finally:
            cursor.close()
            
    def consultarDropDeItemPK(self, Npc:int,numeroItem:int, IDitem:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM dropa WHERE Npc = {Npc} and numeroItem = {numeroItem} and IDitem = {IDitem} ;")
            consulta = cursor.fetchall()

            if not consulta:
                print("Não foi há itens cadastrados\n")
            else:
                for x in consulta:
                    print(x)
                return x
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")
        finally:
            cursor.close()
    
    
    def consultarDropDeItem(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM dropa;")
            consulta = cursor.fetchall()

            if not consulta:
                print("Não foi há DropDeItens cadastrados\n")
            else:
                for x in consulta:
                    print(x)
                return x
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")
        finally:
            cursor.close()
                            
    def deletarDropaItemPK(self, npc:int, numeroItem:int, IDitem:int ):
        try:
            conexao = self.db.conexao
            cursor =  conexao.cursor()
            cursor.execute(f"DELETE FROM dropa WHERE npc = {npc} and numeroItem ={numeroItem} and iditem = {IDitem};")
            delecaoFazMissao = conexao.commit()
            return print("Drop deletado com sucesso!\n")

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a delecao. Erro: {e}\n")
        
        finally:
            cursor.close()
