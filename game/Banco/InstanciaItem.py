import psycopg2
from .Database import Database
from .Item import Item
from .Inventario import Inventario

class Instanciaitem:
    def __init__(self):
        self.db = Database()
    pass

    def inserirInstaciaItem(self, IDitem:int, numeroItem:int,durabilidade:int , IDinv:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Insert into instanciaitem values({IDitem},{numeroItem},{durabilidade},{IDinv});""")
            inserirDropItem = conexao.commit()
            return print("Instancia de item inserido com sucesso")

        except psycopg2.IntegrityError as e:
            print(f"Erro ao inserir Instancia de item", e)
        finally:
            cursor.close()

    def consultarInstanciaItemPK(self, IDitem:int, numeroItem:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM instanciaItem WHERE IDitem = {IDitem} and numeroItem = {numeroItem};")
            consulta = cursor.fetchall()

            if not consulta:
                print("Não foi há instanciaItem cadastrados\n")
            else:
                for x in consulta:
                    print(x)
                return x
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")
        finally:
            cursor.close()
    
    def consultarInstanciaItem(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM Instanciaitem ;")
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
            
    def deletarInstanciaItem(self, IDItem: int, numeroItem:int,):
        try:
            conexao = self.db.conexao
            cursor =  conexao.cursor()
            cursor.execute(f"DELETE FROM instanciaItem WHERE iditem = {IDItem} and numeroitem = {numeroItem};")
            delecaoFazMissao = conexao.commit()
            return print("Instancia de item  deletado com sucesso!\n")

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a delecao. Erro: {e}\n")
        
        finally:
            cursor.close()



item2 = Instanciaitem()
#item2.inserirInstaciaItem(2, 1, 0, 2)

item2.deletarInstanciaItem(2,1)
item2.consultarInstanciaItem()