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
                print("\nParece que você não tem itens do tipo armamento\n")
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
                           f"WHERE i.personagem = '{personagem}' AND ia.iditem = '{IdArma}';")
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
            cursor.execute(f"""SELECT I.IDitem, Ia.numeroitem, I.atcitem  FROM Item I """
                       f"""JOIN InstanciaItem Ia ON I.IDitem = Ia.IDitem """
                       f"""JOIN Inventario Inv ON Ia.IDinv = Inv.IDinv """
                       f"""JOIN Personagem P ON Inv.Personagem = P.IDpersonagem """  # Adicionando um espaço aqui
                       f"""WHERE P.IDpersonagem = {IDpersonagem};""")
            conexao.commit()
            resultado=cursor.fetchall()
            if resultado:
                print(resultado)
        except psycopg2.Error as e:
            print("Erro ao consultar Inventario", e)
        finally:
            cursor.close()

    def verItensInventario(self, IDpersonagem:int):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT I.IDitem, Ia.numeroitem, I.atcitem,
       CASE
           WHEN I.atcitem = 1 THEN T1.nome
           WHEN I.atcitem = 2 THEN T2.nome
           WHEN I.atcitem = 3 THEN T3.nome
       END AS nome,
       CASE
           WHEN I.atcitem = 1 THEN T1.dano
           WHEN I.atcitem = 2 THEN T2.durabilidade
           WHEN I.atcitem = 3 THEN T3.cura
       END AS Dano_Defesa_Durabilidade,
       CASE
           WHEN I.atcitem = 1 THEN T1.elemento
           WHEN I.atcitem = 2 THEN CAST (T2.defesa AS VARCHAR)
           WHEN I.atcitem = 3 THEN CAST (T3.usos AS VARCHAR) 
       END AS Elemento_Defesa_Usos
FROM Item I
JOIN InstanciaItem Ia ON I.IDitem = Ia.IDitem
JOIN Inventario Inv ON Ia.IDinv = Inv.IDinv
JOIN Personagem P ON Inv.Personagem = P.IDpersonagem
LEFT JOIN armamento T1 ON I.atcitem = 1 AND T1.item = I.IDitem
LEFT JOIN armadura T2 ON I.atcitem = 2 AND T2.item  = I.IDitem
LEFT JOIN consumivel T3 ON I.atcitem = 3 AND T3.item  = I.IDitem
WHERE P.IDpersonagem = {IDpersonagem};""")
            conexao.commit()
            resultado=cursor.fetchall()
            if resultado:
                print(resultado)
        except psycopg2.Error as e:
            print("Erro ao consultar Inventario", e)
        finally:
            cursor.close()
    