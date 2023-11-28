import psycopg2
from Database import Database

class Armadura:
    def __init__(self):
        self.db = Database()
    pass
    
    def inserirArmadura(self, item: int, nome: str, durabilidade: int, defesa: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()

            cursor.execute("INSERT INTO armadura VALUES(%s, %s, %s, %s);", (item, nome, durabilidade, defesa))
            insercaoArmamento = conexao.commit()
            return print("Armadura inserida com sucesso!\n")

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a insercao. Erro: {e}\n")
        
        finally:
            cursor.close()

    def deletarArmadura(self, item: int):
        try:
            conexao = self.db.conexao
            cursor =  conexao.cursor()

            cursor.execute(f"DELETE FROM armadura WHERE item = '{item}';")
            delecaoArmamento = conexao.commit()
            return print("Armadura deletada com sucesso!\n")
        
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a delecao. Erro: {e}\n")
        
        finally:
            cursor.close()

    def consultarArmaduraId(self, item: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            
            cursor.execute(f"SELECT * FROM armadura WHERE item = '{item}';")
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

    def consultarArmadura(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            
            cursor.execute(f"SELECT * FROM armadura;")
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

