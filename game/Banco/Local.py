import psycopg2
from .Database import Database
from .Mundo import Mundo
from .Regiao import Regiao


class Local :
    def __init__(self):
        self.db = Database()
    pass
    
    def inserirLocal(self,coordenada:int, descrição:str,nome:str,tipo:bool,regiao:str):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Insert into local values({coordenada},'{descrição}','{nome}',{tipo},'{regiao}');""")
            insercaoMundo = conexao.commit()
            return print("Local inserido com sucesso")
        except psycopg2.Error as e:
            print("Erro ao inserir em Local", e)
        finally:
            cursor.close()
    
    def deletarLocal(self, coordenada:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""delete from local where coordenada = {coordenada};""")
            delecaoMundo = conexao.commit()
            return print("Local deletado com sucesso")
        except psycopg2.Error as e:
            print("Erro ao deletar em Local", e)
        finally:
            cursor.close()

    def consultarLocal(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"Select * from local;")
            consultaLocal = cursor.fetchall()
            for x in consultaLocal:
                print(x)
            return x
        except psycopg2.Error as e:
            print("Erro ao consultar local", e)
        finally:
            cursor.close()
    
    def consultarLocalCoordenada(self,coordena:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"Select * from local where coordenada = {coordena};")
            consultaLocal = cursor.fetchall()
            for x in consultaLocal:
                print(x)
            return x
        except psycopg2.Error as e:
            print("Erro ao consultar local", e)
        finally:
            cursor.close()
    
    def getLocal(self,coordena:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"Select * from local where coordenada = {coordena};")
            consultaLocal = cursor.fetchall()
            if(consultaLocal == []):
                return None
            else:
                return consultaLocal
        except psycopg2.Error as e:
            print("Erro ao consultar local", e)
        finally:
            cursor.close()
                
    def getLocalPc(self,personagem:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"select l.coordenada , l.descricao , l.nome , l.tipo , l.regiao from local l join pc p on l.coordenada = p.local where p.personagem = {personagem};")
            consultaLocal = cursor.fetchall()
            if(consultaLocal == []):
                return None
            else:
                return consultaLocal
        except psycopg2.Error as e:
            print("Erro ao consultar local", e)
        finally:
            cursor.close()

    def verMissaoLocal(self,local:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute( f"SELECT local_missao_contem.local, local_missao_contem.missao, "
                            f"descricao_recompensa_missao.descricao, descricao_recompensa_missao.recompensa "
                            f"FROM ("
                            f"   SELECT c.local, c.missao "
                            f"   FROM contem c "
                            f"   LEFT JOIN local l ON c.local = l.coordenada"
                            f"   where l.coordenada = {local}   "     
                            f") AS local_missao_contem "
                            f"Left join("
                            f"   SELECT m.nome, m.descricao, m.recompensa "
                            f"   FROM missao m "
                            f"   INNER JOIN contem c ON c.missao = m.nome"
                            f") AS descricao_recompensa_missao "
                            f"ON local_missao_contem.missao = descricao_recompensa_missao.nome;")
            consultaLocal = cursor.fetchall()
            if not consultaLocal:
                print("\nNão há missão nesse local\n")
            else:
                print("\033[1;32mMissao Disponível!\033[0m")
                return consultaLocal
        except psycopg2.Error as e:
            print("Erro ao consultar local", e)
        finally:
            cursor.close()
        