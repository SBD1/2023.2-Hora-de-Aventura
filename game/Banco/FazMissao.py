import psycopg2
from .Database import Database

class FazMissao:
    def __init__(self):
        self.db = Database()
    pass

    def inserirFazMissao(self, personagem: int, nomeMissao: str, status: bool):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()

            cursor.execute("INSERT INTO fazmissao VALUES(%s, %s, %s);", (personagem, nomeMissao, status))
            insercaoFazMissao = conexao.commit()
            return print("Missao inserida com sucesso!\n")

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")
        
        finally:
            cursor.close()

    def deletarFazMissao(self, personagem: int):
        try:
            conexao = self.db.conexao
            cursor =  conexao.cursor()

            cursor.execute(f"DELETE FROM fazmissao WHERE personagem = '{personagem}';")
            delecaoFazMissao = cursor.commit()
            return print("Missao deletada com sucesso!\n")
        
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")
        
        finally:
            cursor.close()

    def deletarFazMissaoEspecifica(self, personagem: int, nomeMissao: str):
        try:
            conexao = self.db.conexao
            cursor =  conexao.cursor()

            cursor.execute(f"DELETE FROM fazmissao WHERE personagem = '{personagem}' AND nomemissao = '{nomeMissao}';")
            delecaoFazMissao = conexao.commit()
            return print("Missao deletada com sucesso!\n")
        
        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")
        
        finally:
            cursor.close()        

    def consultarFazMissao(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM fazmissao;")
            consulta = cursor.fetchall()

            if not consulta:
                print("Não foi possivel acessar a tabela\n")
            else:
                for i in consulta:
                    print(i)
                return i

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")

        finally:
            cursor.close()

    def consultarFazMissaoPersonagem(self, personagem: int):
        try:    
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM fazmissao WHERE personagem = '{personagem}';")
            consulta = cursor.fetchall()

            if not consulta:
                print("Não foi encontrada nenhuma missao desse personagem\n")
            else:
                for i in consulta:
                    print(i)
                return i

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")

        finally:
            cursor.close()

    def consultarFazMissaoNome(self, nome: str):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM fazmissao WHERE nomemissao = '{nome}';")
            consulta = cursor.fetchall()

            if not consulta:
                print("Não foi encontrada nenhuma missao com esse nome\n")
            else:
                for i in consulta:
                    print(i)
                return i

        except psycopg2.IntegrityError as e:
            print(f"Encontramos problemas ao fazer a consulta. Erro: {e}\n")

        finally:
            cursor.close()

