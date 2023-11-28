import psycopg2
from .Database import Database


class Personagem: 
    def __init__(self):
        self.db = Database()
    pass
        
    def criarPersonagem(self, IDpersonagem,ATC:bool):
        try:    
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""insert into personagem values({IDpersonagem},{ATC});""")
            insercaoPersonagem = conexao.commit()
            return print("Personagem criado com sucesso")
        except psycopg2.Error as e: 
            print("Erro ao inserir personagem", e)
        finally:
            cursor.close()     
    
    def consultarPersonagem(self):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Select * from personagem;""")
            consultarPersonagem = cursor.fetchall() 
            for x in consultarPersonagem:
                print(x)
              
        except psycopg2.Error as e:
            print("")
        finally:
            cursor.close()

    def consultarPersonagemID(self, IDpersonagem:int):
        try:
            conexao = self.db.conexao 
            cursor = conexao.cursor()
            cursor.execute(f"""Select * from personagem where IDpersonagem = {IDpersonagem};""")    
            consultarPersonagemID = cursor.fetchall()
            if(consultarPersonagemID == []):
                print('Não possui esse personagem')
            else:
                for x in consultarPersonagemID:
                    print(x)
        except psycopg2.Error as e : 
            print("Erro ao consultar personagem por ID:", e )            
        finally: 
            cursor.close() 
            
    def deletarPersonagem(self, IDpersonagem:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            query = cursor.execute(f"""delete from personagem where IDpersonagem = {IDpersonagem};""") 
            conexao.commit()
            query_exec = query 
        except psycopg2.Error as e:
            print("Erro ao deletar em Mundo", e)
        finally:       
               cursor.close()
    
        
                