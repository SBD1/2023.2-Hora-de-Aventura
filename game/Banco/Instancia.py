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

    def atualizarVidaInstanciaID(self, IDinstancia: int, numeroInstancia: int, novaVida: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""UPDATE instancia SET vida = '{novaVida}' WHERE personagem = '{IDinstancia}' AND numero = '{numeroInstancia}'; """)
            linhas_afetadas = cursor.rowcount
            conexao.commit()  

            if linhas_afetadas == 0:
                print("Não há dados na tabela que correspondam à condição de atualização.")
        except psycopg2.Error as e:
            print("Erro ao atualizar a vida da instância:", e)
        finally:
            cursor.close()

    def     getInstanciasLocais(self, localAtual: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT i.personagem, i.numero, n.nome, n.lvl, n.especie FROM instancia i JOIN npc n ON i.personagem = n.personagem WHERE i.local = '{localAtual}' and conduta = true;")
            monstros_no_local = cursor.fetchall()

            if not monstros_no_local:
                print("Felizmente, nenhum inimigo por aqui!\n")
            else:
                print("\033[1;32mMonstros no local:\033[0m")
                for instancia in monstros_no_local:
                    id_instancia = instancia[0]
                    num_instancia = instancia[1]
                    nome_instancia = instancia[2].strip()
                    lvl_instancia = instancia[3]
                    esp_instancia = instancia[4].strip()  
                    print(f"Nome = {nome_instancia}, lvl = {lvl_instancia}, Espécie = {esp_instancia} -- ID = {id_instancia} Num = {num_instancia}")
                return monstros_no_local

        except psycopg2.Error as e:
            print("Não foi possivel fazer essa consulta")

        finally:
            cursor.close()

    def conferirInstanciaDoLocalPersonagem(self, localAtual: int, ID: int, Num: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT i.personagem, i.numero, n.nome, n.lvl, n.especie FROM instancia i JOIN npc n ON i.personagem = n.personagem WHERE i.local = '{localAtual}' and n.conduta = true and i.personagem = '{ID}' and i.numero = '{Num}';")
            monstros_no_local2 = cursor.fetchall()

            if not monstros_no_local2:
                print("\n")
            else:
                return monstros_no_local2

        except psycopg2.IntegrityError as e:
            print("aaaaaaaaaaaa")
        
        finally:
            cursor.close()

    def getInstanciaID(self, personagem: int, numero: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM instancia WHERE personagem = '{personagem}' AND numero = '{numero}';")
            consulta = cursor.fetchall()
            if consulta:
                return consulta

        except psycopg2.Error as e:
            print("Não foi possivel fazer essa consulta")

        finally:
            cursor.close()
