import psycopg2
from .Database import Database
from .Personagem import Personagem
from .Local import Local


class Pc:
    def __init__(self):
        self.db = Database()
        pass
    
    def criarPc(self, nome:str,
                 xp:int,vida:int,lvl:int,dinheiro:int,especie:str,forca:int,defesa:int,local:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"INSERT INTO pc VALUES((SELECT COALESCE(MAX(idpersonagem ), 0) FROM personagem),'{nome}', {xp},{vida},{lvl},{dinheiro},'{especie}',{forca},{defesa},{local});")

            conexao.commit()
            conexao.commit()
        except psycopg2.Error as e:
            print("Erro ao criar os PC's", e )
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

    def getPCbyID(self, id: int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""SELECT * FROM pc WHERE personagem = '{id}' ; """)
            busca = cursor.fetchall() 
            if busca:
                return busca
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

    def updatePcXp(self,Personagem:int, Xp:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""update pc set xp = {Xp} where personagem = {Personagem};""")
            conexao.commit()
        except psycopg2.Error as e:
            print("Erro ao cosultar os PC's", e )
        finally:
            cursor.close()

    def updatePcDinheiro(self,Personagem:int, Dinheiro:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""update pc set dinheiro = {Dinheiro} where personagem = {Personagem};""")
            conexao.commit()
        except psycopg2.Error as e:
            print("Erro ao cosultar os PC's", e )
        finally:
            cursor.close()

    def PcSubirNivel(self,Personagem:int,xp:int,lvl:int,vida:int,forca:int,defesa:int ):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"begin transaction;"
                            f"update pc set xp = {xp} where personagem = {Personagem};"
                            f"update pc set lvl = {lvl} where personagem = {Personagem};"
                            f"update pc set vida = {vida} where personagem = {Personagem};"
                            f"update pc set forca = {forca} where personagem = {Personagem};"
                            f"update pc set defesa = {defesa} where personagem = {Personagem};"
                            f"commit;"
                            f"end transaction;")
            conexao.commit()
        except psycopg2.Error as e:
            print("Erro ao cosultar os PC's", e )
        finally:
            cursor.close()

    def atribuirMissaoAoJogador(self, pcID, missaoNome):
        lc = Local()

        
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(
                f"INSERT INTO fazMissao VALUES ({pcID}, '{missaoNome}', False);")
            conexao.commit()
            print("Missão atribuída ao jogador e registrada.")
        except psycopg2.Error as e:
            print("Erro ao inserir na tabela fazMissao", e)
        finally:
            cursor.close()
