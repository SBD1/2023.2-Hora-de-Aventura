import psycopg2
from typing import Optional
from .Database import Database

class Instancia:
    
    def __init__(self, personagem: int, numero: int, vida: int, local: int, idPersonagem: int):
        self.personagem = personagem
        self.numero = numero
        self.vida = vida
        self.local = local
        self.idPersonagem = idPersonagem
    pass

    def __init__(self):
        self.db = Database()
    pass

    def inserirInstancia(self, personagem: int, numero: int, vida: int, local: int, idPersonagem: Optional[int]):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()

            # Ussando a formatação %s porque assim o psycop trata a tipagem e permite argumento None, pra quando
            # algo precisar ser nulo
            ## i.inserirInstancia(3, 3, 37, 1, None) -> exemplo do None
            cursor.execute("INSERT INTO instancia VALUES (%s, %s, %s, %s, %s);", (personagem, numero, vida, local, idPersonagem))
            insercaoInstancia = conexao.commit()
            return print("Instancia criada com sucesso!\n")
            
        except psycopg2.IntegrityError as e:
            print("Não foi possível inserir instancia na tabela: ", e)
            
        finally:
            cursor.close()

    def deletarInstancia(self, personagem: int, numero: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"DELETE FROM instancia WHERE personagem = '{personagem}' AND numero = '{numero}';")
            delecaoInstacia = conexao.commit()
            return print("Instacia deletada com sucesso")
        
        except psycopg2.Error as e:
            print("Erro ao deletar em instancia", e)
        
        finally:
            cursor.close()            
    
    def consultarInstancia(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM instancia;")
            consulta = cursor.fetchall()
            if not consulta:
                print("Nao foi possivel ver instancias")
            else:
                for x in consulta:
                    print(x)
                return x
        
        except psycopg2.Error as e:
            print("Erro ao executar a consulta:", e)
        
        finally:
            cursor.close()

    def consultarInstanciaPersonagem(self, personagem: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM instancia WHERE personagem = '{personagem}';")
            consulta = cursor.fetchall()

            if not consulta:
                print("Não há nenhuma instancia com essas caracteristicas\n")
            else:
                for i in consulta:
                    print(i)
                return i

        except psycopg2.Error as e:
            print("Não foi possivel fazer essa consulta")

        finally:
            cursor.close()

    def consultarInstanciaEspecifica(self, personagem: int, numero: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM instancia WHERE personagem = '{personagem}' AND numero = '{numero}';")
            consulta = cursor.fetchall()

            if not consulta:
                print("Não há nenhuma instancia com essas caracteristicas\n")
            else:
                for i in consulta:
                    print(i)
                return i

        except psycopg2.Error as e:
            print("Não foi possivel fazer essa consulta")

        finally:
            cursor.close()

## i = Instancia()
## i.consultarInstancia()



