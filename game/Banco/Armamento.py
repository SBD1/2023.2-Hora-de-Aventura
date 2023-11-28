import psycopg2
from Database import Database

class Armamento:
    def __init__(self, item: int, nome: str, dano: int, elemento: str):
        self.item = item
        self.nome = nome
        self.dano = dano
        self.elemento = elemento
    pass

    def __init__(self):
        self.db = Database()
    pass

    def inserirArmamento(self, item: int, nome: str, dano: int, elemento: str):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()

            cursor.execute("INSERT INTO armamento VALUES(%s, %s, %s, %s);", (item, nome, dano, elemento))
            insercaoArmamento = conexao.commit()
            return print("Arma inserida com sucesso!\n")

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a insercao. Erro: {e}\n")
        
        finally:
            cursor.close()

    def deletarArmamento(self, item: int):
        try:
            conexao = self.db.conexao
            cursor =  conexao.cursor()

            cursor.execute(f"DELETE FROM armamento WHERE item = '{item}';")
            delecaoArmamento = conexao.commit()
            return print("Arma deletada com sucesso!\n")
        
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a delecao. Erro: {e}\n")
        
        finally:
            cursor.close()

    def consultarArmamentoId(self, item: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM armamento WHERE item = '{item}';")
            consulta = cursor.fetchall()

            if not consulta:
                print("Não foi há armas cadastradas\n")
            else:
                for i in consulta:
                    print(i)
                return i

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")

        finally:
            cursor.close()

    def consultarArmamento(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM armamento;")
            consulta = cursor.fetchall()

            if not consulta:
                print("Não foi há armas cadastradas\n")
            else:
                for i in consulta:
                    print(i)
                return i

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")

        finally:
            cursor.close()

a = Armamento()
a.consultarArmamentoId(1)