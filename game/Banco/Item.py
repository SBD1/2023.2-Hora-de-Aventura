import psycopg2
from Database import Database

class Item:
    
    def __init__(self, idItem: int, atcItem: int):
        self.idItem = idItem
        self.atcItem = atcItem
    pass

    def __init__(self):
        self.db = Database()
    pass

    def inserirItem(self, idItem: int, atcItem: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()

            cursor.execute("INSERT INTO item VALUES(%s, %s);", (idItem, atcItem))
            insercaoFazMissao = conexao.commit()
            return print("Item inserido com sucesso!\n")

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a insercao. Erro: {e}\n")
        
        finally:
            cursor.close()

    def deletarItem(self, idItem: int):
        try:
            conexao = self.db.conexao
            cursor =  conexao.cursor()

            cursor.execute(f"DELETE FROM item WHERE iditem = '{idItem}';")
            delecaoFazMissao = cursor.commit()
            return print("Item deletado com sucesso!\n")
        
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a delecao. Erro: {e}\n")
        
        finally:
            cursor.close()

    def consultarItemId(self, idItem: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM item WHERE iditem = '{idItem}';")
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

