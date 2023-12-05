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
        except psycopg2.Error as e: 
            print("Erro ao inserir PC", e)
        finally:
            cursor.close()     
    
    def consultarPC(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""SELECT * FROM PC; """)
            consultarPC = cursor.fetchall() 
            if not consultarPC:
                print("Não existe nenhum PC")
            else:
                for pc in consultarPC:
                    id = pc[0]
                    nome = pc[1]
                    xp = pc[2]
                    pv = pc[3]
                    lvl = pc[4]
                    dinheiro = pc[5]
                    especie = pc[6]
                    forca = pc[7]
                    defesa = pc[8]
                    local = pc[9]
                    print(f"{id},  {nome},  {xp},   {pv},   {lvl},   {dinheiro},  {especie}, {forca},   {defesa},     {local}")
                print("\n")
        except psycopg2.Error as e:
            print("Erro ao consultar os PCs:", e)
        finally:
            cursor.close()

                
    def consultarPCNome(self, Nome:str):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Select * from PC where nome = '{Nome}'; """)
            consultarPC = cursor.fetchall() 
            return consultarPC
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

                
    def deletarPC(self, IDpersonagem:int):
        try:     
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""delete from pc where personagem = {IDpersonagem}""")
            conexao.commit() 
        except psycopg2.Error as e:
            print("Erro ao deletar PC", e )
        finally:
            cursor.close()
    
            
    def updatePc(self,Personagem:int, Nome:set):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""update pc set nome = '{Nome}' where personagem = {Personagem};""")
            conexao.commit()
        except psycopg2.Error as e:
            print("Erro ao atualizar pc's ", e )
        finally:
            cursor.close()

        
            
            
    def updatePcLocal(self,Personagem:int, Local:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""update pc set local = {Local} where personagem = {Personagem};""")
            conexao.commit()
        except psycopg2.Error as e:
            print("Erro ao cosultar os PC's", e )
        finally:
            cursor.close()
