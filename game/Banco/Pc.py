import psycopg2
from .Database import Database
from .Personagem import Personagem


class Pc:
    def __init__(self):
        self.db = Database()
        pass
    
    def criarPc(self, personagem:int, nome,
                 xp:int,vida:int,lvl:int,dinheiro:int,especie,forca:int,defesa:int,local:int):    
        try:    
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""insert into pc values({personagem},'{nome}',{xp},
                           {vida},{lvl},{dinheiro},'{especie}',{forca},{defesa},{local});""")
            conexao.commit()
            return print("\nPersonagem criado com sucesso")
        except psycopg2.Error as e: 
            print("Erro ao inserir PC", e)
        finally:
            cursor.close()     
    
    def consultarPC(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Select * from PC; """)
            consultarNPC = cursor.fetchall() 
            if(consultarNPC == []):
                print("Não existe nenhum PC")
            else:
                for x in consultarNPC:
                    print(x)
        except psycopg2.Error as e:
            print("Erro ao cosultar os PC's", e )
        finally:
                cursor.close()
                
    def consultarPCID(self,Personagem:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Select * from PC where personagem = {Personagem}; """)
            consultarNPC = cursor.fetchall() 
            if(consultarNPC == []):
                print("Não existe nenhum PC com esse ID ")
            else:
                for x in consultarNPC:
                    print(x)
        except psycopg2.Error as e:
            print("Erro ao cosultar os PC's", e )
        finally:
            cursor.close()

    def atualizarVidaPCID(self,personagem: int, novaVida: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""UPDATE pc SET vida = {novaVida} where personagem = '{personagem}'; """)
            linhas_afetadas = cursor.rowcount
            conexao.commit()  

            if linhas_afetadas == 0:
                print("Não há dados na tabela que correspondam à condição de atualização.")
        except psycopg2.Error as e:
            print("Erro ao atualizar a vida do pc:", e)
        finally:
            cursor.close()
        
    def getPC(self,Personagem:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Select * from PC where personagem = {Personagem}; """)
            consultarPC = cursor.fetchall()
            if(consultarPC == []):
                print("Não existe nenhum PC com esse ID ")
            else:
                return consultarPC
        except psycopg2.Error as e:
            print("Erro ao cosultar os PC's", e )
        finally:
            cursor.close()

                
    def deletarNPC(self, IDpersonagem:int):
        try:     
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""delete from npc where personagem = {IDpersonagem}""")
            conexao.commit() 
        except psycopg2.Error as e:
            print("Erro ao deletar NPC", e )
        finally:
            cursor.close()
            
    def updatePcLocal(self,Personagem:int, Local:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""update pc set local = {Local} where personagem = {Personagem}; """)
            consultarNPC = cursor.fetchall() 
            if(consultarNPC == []):
                print("Não existe nenhum PC com esse ID ")
            else:
                return consultarNPC
        except psycopg2.Error as e:
            print("Erro ao cosultar os PC's", e )
        finally:
            cursor.close()
            
