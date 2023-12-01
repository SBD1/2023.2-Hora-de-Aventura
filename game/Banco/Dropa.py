import psycopg2
from Database import Database
from Npc import Npc
from Item import Item


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


    def consultarDropDeItem(self, Npc:int,numeroItem:int, IDitem:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM item WHERE Npc ;")
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

    def consultarItem(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM item;")
            consulta = cursor.fetchall()

            if not consulta:
                print("Não foi há itens cadastrados\n")
            else:
                for i in consulta:
                    print(i)
                return i

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")

        finally:
            cursor.close()

    def deletarItem(self, idItem: int):
        try:
            conexao = self.db.conexao
            cursor =  conexao.cursor()

            cursor.execute(f"DELETE FROM item WHERE iditem = '{idItem}';")
            delecaoFazMissao = conexao.commit()
            return print("Item deletado com sucesso!\n")
        
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a delecao. Erro: {e}\n")
        
        finally:
            cursor.close()
