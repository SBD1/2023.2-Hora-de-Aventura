import psycopg2
from Database import Database

class Consumivel:

    def __init__(self):
        self.db = Database()
    pass

    def inserirConsumivel(self, item: int, nome: str, cura: int, usos: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()

            cursor.execute("INSERT INTO consumivel VALUES(%s, %s, %s, %s);", (item, nome, cura, usos))
            conexao.commit()
            return print("Consumivel inserido com sucesso!\n")

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a insercao. Erro: {e}\n")
        
        finally:
            cursor.close()

    def deletarConsumivel(self, item: int):
        try:
            conexao = self.db.conexao
            cursor =  conexao.cursor()

            cursor.execute(f"DELETE FROM consumivel WHERE item = '{item}';")
            delecaoArmamento = conexao.commit()
            return print("Consumivel deletado com sucesso!\n")
        
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a delecao. Erro: {e}\n")
        
        finally:
            cursor.close()

    def consultarConsumivelId(self, item: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM consumivel WHERE item = '{item}';")
            consulta = cursor.fetchall()

            if not consulta:
                print("Não tem consumiveis cadastradas\n")
            else:
                for i in consulta:
                    print(i)
                return i

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")

        finally:
            cursor.close()

    def consultarConsumivel(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM consumivel;")
            consulta = cursor.fetchall()

            if not consulta:
                print("Não tem cosnsumiveis cadastradas\n")
            else:
                for i in consulta:
                    print(i)
                return i

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")

        finally:
            cursor.close()

c = Consumivel()
c.inserirConsumivel(2, "Poção de vida", 30, 1)
c.consultarConsumivelId(2)