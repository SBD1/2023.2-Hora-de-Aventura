import psycopg2
from .Database import Database
from .Item import Item
from .Inventario import Inventario

class PosuuiItem:
    def __init__(self):
        self.db = Database()
    pass

    def inserirPossuiItem(self, IDitem:int, loja:str, tipo:str ,precoItem:int ):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Insert into possuiitem values({IDitem},'{loja}','{tipo}',{precoItem});""")
            inserirDropItem = conexao.commit()
            return print("possuiitem inserido com sucesso")

        except psycopg2.IntegrityError as e:
            print(f"Erro ao inserir possuiitem", e)
        finally:
            cursor.close()

    def consultarPossuiItemPK(self, IDitem:int, loja:str, tipo:str):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM possuiItem WHERE IDitem = {IDitem} and loja = '{loja}' and tipo = '{tipo}';")
            consulta = cursor.fetchall()

            if not consulta:
                print("Não foi há possuiItem cadastrados\n")
            else:
                for x in consulta:
                    print(x)
                return x
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")
        finally:
            cursor.close()
    
    def consultarPossuiItem(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM possuiItem ;")
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
            
    def deletarPossuiItem(self, IDitem:int, loja:str, tipo:str):
        try:
            conexao = self.db.conexao
            cursor =  conexao.cursor()
            cursor.execute(f"DELETE FROM possuiItem WHERE iditem = {IDitem} and numeroitem = '{loja}' and tipo = '{tipo}';")
            delecaoFazMissao = conexao.commit()
            return print("PossuiItem  deletado com sucesso!\n")

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a delecao. Erro: {e}\n")
        
        finally:
            cursor.close()


pI = PosuuiItem()

#pI.inserirPossuiItem(1, 'Loja de Arma', 'Espadas', 100)

#pI.consultarPossuiItemPK(1,'Loja de Arma', 'Espadas')

#pI.consultarPossuiItemPK(1,'Loja de Arma', 'Espadas')