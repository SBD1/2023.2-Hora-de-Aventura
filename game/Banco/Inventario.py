import psycopg2
from .Database import Database

class Inventario:
    def __init__(self):
        self.db=Database()

    def inserirInventario(self, IDinv:int, QTD_de_itens:int, Personagem:int):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""INSERT INTO Inventario VALUES({IDinv}, '{QTD_de_itens}', {Personagem});""")
            conexao.commit()
            return print("Inventario Inserido")
        except psycopg2.Error as e:
            print("Erro ao inserir Inventario", e)
        finally:
            cursor.close()
    
    def consultarInventario(self):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT * FROM Inventario;""")
            conexao.commit()
            resultado=cursor.fetchall()
            for i in resultado:
                print(i)
        except psycopg2.Error as e:
            print("Erro ao consultar Inventario", e)
        finally:
            cursor.close()

    def deletarInventario(self, IDinv:int):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""DELETE FROM Inventario WHERE IDinv = {IDinv};""")
            conexao.commit()
            return print("Inventario Deletada")
        except psycopg2.Error as e:
            print("Erro ao deletar Inventario", e)
        finally:
            cursor.close()

    def consultarInventarioEspecifico(self, IDinv:int):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT * FROM Inventario WHERE IDinv = {IDinv};""")
            conexao.commit()
            resultado=cursor.fetchall()
            if resultado:
                print(resultado[0])
        except psycopg2.Error as e:
            print("Erro ao consultar Inventario", e)
        finally:
            cursor.close()
    
    def consultarInventarioArmasID(self,personagem: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT ia.iditem, ar.nome, ar.dano "
                           f"FROM instanciaitem ia "
                           f"JOIN inventario i ON ia.idinv = i.idinv "
                           f"JOIN armamento ar ON ia.iditem = ar.item "
                           f"WHERE i.personagem = '{personagem}';")
            consulta = cursor.fetchall()
            if consulta:
                for x in consulta:
                    print(x)
            else: 
                print("Parece que você não tem itens do tipo armamento\n")
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")
        finally:
            cursor.close()

    def getInventarioArmasID(self,personagem: int, IdArma: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT ia.iditem, ar.nome, ar.dano "
                           f"FROM instanciaitem ia  "
                           f"JOIN inventario i ON ia.idinv = i.idinv "
                           f"JOIN armamento ar ON ia.iditem = ar.item "
                           f"WHERE i.personagem = '{personagem}';")
            consulta = cursor.fetchall()
            if consulta:
                return consulta
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")
        finally:
            cursor.close()

    def consultarInventarioConsumiveisID(self,personagem: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT ia.iditem, po.nome, po.cura, po.usos "
                           f"FROM instanciaitem ia "
                           f"JOIN inventario i ON ia.idinv = i.idinv "
                           f"JOIN consumivel po ON ia.iditem = po.item "
                           f"WHERE i.personagem = '{personagem}';")
            consulta = cursor.fetchall()
            if consulta:
                for x in consulta:
                    print(x)
            else: 
                print("Parece que você não tem itens do tipo Consumivel\n")
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")
        finally:
            cursor.close()

    def getInventarioConsumiveisID(self,personagem: int, IdPocao: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT ia.iditem, po.nome, po.cura, po.usos "
                           f"FROM instanciaitem ia "
                           f"JOIN inventario i ON ia.idinv = i.idinv "
                           f"JOIN consumivel po ON ia.iditem = po.item "
                           f"WHERE i.personagem = '{personagem}' AND po.item = '{IdPocao}';")
            consulta = cursor.fetchall()
            if consulta:
                return consulta
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")
        finally:
            cursor.close()
            
    def verItensInventario(self, IDpersonagem:int):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT I.IDitem  FROM Item I """
                       f"""JOIN InstanciaItem Ia ON I.IDitem = Ia.IDitem """
                       f"""JOIN Inventario Inv ON Ia.IDinv = Inv.IDinv """
                       f"""JOIN Personagem P ON Inv.Personagem = P.IDpersonagem """  # Adicionando um espaço aqui
                       f"""WHERE P.IDpersonagem = {IDpersonagem};""")
            conexao.commit()
            resultado=cursor.fetchall()
            if resultado:
                print(resultado[0])
        except psycopg2.Error as e:
            print("Erro ao consultar Inventario", e)
        finally:
            cursor.close()
