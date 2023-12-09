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

    def getItensLoja(self, LojaNome: str):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"select ps.iditem, ar.nome, ps.loja, ps.precoitem from possuiitem ps " 
                           f"JOIN armamento ar ON ps.iditem = ar.item "
                           f"where ps.loja = '{LojaNome}' "
                           f"union "
                           f"select ps.iditem, arm.nome, ps.loja, ps.precoitem from possuiitem ps "
                           f"JOIN armadura arm ON ps.iditem = arm.item "
                           f"where ps.loja = '{LojaNome}' "
                           f"union "
                           f"select ps.iditem, cons.nome, ps.loja, ps.precoitem from possuiitem ps "
                           f"JOIN consumivel cons ON ps.iditem = cons.item "
                           f"where ps.loja = '{LojaNome}'; ")

            conexao.commit()
            lojaItens = cursor.fetchall()
            if lojaItens:
                print("\033[1;32m\nItens:\n\033[0m")
                for item in lojaItens:
                    idItem = item[0] 
                    nome = item[1].strip()
                    preco = item[3]
                    print(f"\033[1;32midItem\033[0m = {idItem}, \033[1;32mNome\033[0m = {nome}, \033[1;32mPreco\033[0m = {preco}")
                return lojaItens
        except psycopg2.IntegrytError as e:
            print("Erro ao consultar Loja", e)
        finally:
            cursor.close()
        
    def getItemDaLoja(self, LojaNome: str, iditem: int):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"select ps.iditem, ar.nome, ps.loja, ps.precoitem from possuiitem ps " 
                           f"JOIN armamento ar ON ps.iditem = ar.item "
                           f"where ps.loja = '{LojaNome}' and  iditem = '{iditem}' "
                           f"union "
                           f"select ps.iditem, arm.nome, ps.loja, ps.precoitem from possuiitem ps "
                           f"JOIN armadura arm ON ps.iditem = arm.item "
                           f"where ps.loja = '{LojaNome}' and  iditem = '{iditem}' "
                           f"union "
                           f"select ps.iditem, cons.nome, ps.loja, ps.precoitem from possuiitem ps "
                           f"JOIN consumivel cons ON ps.iditem = cons.item "
                           f"where ps.loja = '{LojaNome}' and  iditem = '{iditem}' ;")

            conexao.commit()
            lojaItens = cursor.fetchall()
            if lojaItens:
                print("\033[1;32m\nIten Selecionado:\n\033[0m")
                for item in lojaItens:
                    idItem = item[0] 
                    nome = item[1].strip()
                    preco = item[3]
                    print(f"\033[1;33midItem\033[0m = {idItem}, \033[1;33mNome\033[0m = {nome}, \033[1;33mPreco\033[0m = {preco}")
                return lojaItens
        except psycopg2.IntegrytError as e:
            print("Erro ao consultar Loja", e)
        finally:
            cursor.close()
    
    def compraDoItem(self, iditem: int, idInventario: int, novoSaldo: int, IDpersonagem:int):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute( f"BEGIN TRANSACTION; "
                            f"INSERT INTO instanciaItem "
                            f"VALUES ( "
                            f"'{iditem}', "
                            f"COALESCE((SELECT MAX(numeroitem) FROM instanciaItem WHERE IdItem = '{iditem}'), 0) + 1, "
                            f"10, "
                            f"'{idInventario}'); "
                            f"UPDATE pc SET dinheiro = '{novoSaldo}' WHERE {IDpersonagem} = 40; "
                            f"COMMIT; ")
            conexao.commit()
            
        except psycopg2.IntegrytError as e:
            print("Erro ao consultar Loja", e)
        finally:
            cursor.close()