import psycopg2
from .Database import Database
from .Personagem import Personagem


class Npc:
    def __init__(self):
        self.db = Database()
        pass
    
    def criarNpc(self, personagem:int, nome:str,vidaMax:int, conduta:bool,lvl:int,especie:str,forca:int, defesa:int):    
        try:    
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""insert into npc values({personagem},'{nome}',{vidaMax},
                           {conduta},{lvl},'{especie}',{forca},{defesa});""")
            conexao.commit()
            return print("NPC criado com sucesso")
        except psycopg2.Error as e: 
            print("Erro ao inserir NPC", e)
        finally:
            cursor.close()     
    
    def consultarNPC(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Select * from NPC; """)
            consultarNPC = cursor.fetchall() 
            if(consultarNPC == []):
                print("Não existe nenhum NPC")
            else:
                for x in consultarNPC:
                    print(x)
        except psycopg2.Error as e:
            print("Erro ao cosultar os NPC's", e )
        finally:
                cursor.close()
                
    def consultarNPCID(self,Personagem:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Select * from NPC where personagem = {Personagem}; """)
            consultarNPC = cursor.fetchall() 
            if(consultarNPC == []):
                print("Não existe nenhum NPC com esse ID ")
            else:
                for x in consultarNPC:
                    print(x)
        except psycopg2.Error as e:
            print("Erro ao cosultar os NPC's", e )
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
            
                
            