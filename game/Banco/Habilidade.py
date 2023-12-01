import psycopg2 
from Database import Database


class Habilidade:
    def __init__(self): 
        self.db = Database() 
        pass
    
    def consultarHabildade(self):
        try:    
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM habilidade;")
            consultaHabildade = cursor.fetchall()
            if(consultaHabildade == []):
                print("Não foi possivel consultar habildade")
            else:
                for x in consultaHabildade:
                    print(x)
        except psycopg2.Error as e:
            print("Erro ao consultar Habilidade:", e)
        finally:
            cursor.close()
    
    
    def inserirHabilidade(self,IDhabilidade:int, nome:str, tempoDeRecarga:int, dano:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Insert into habilidade values({IDhabilidade},'{nome}',
                           {tempoDeRecarga},{dano});""")
            insercaoHabilidade = conexao.commit()
            return print("Habilidade criada com sucesso")
        except psycopg2.Error as e:
            print("Erro ao criar Habilidade ", e)
        finally:
            cursor.close()
    
              
    def consultarHabilidadeID(self,IDhabilidade:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Select * from habilidade where IDhabilidade = {IDhabilidade};""")
            consultaHabilidade = cursor.fetchall()
            if(consultaHabilidade == []):
                print("Erro ao consultar habilidade por ID")
            else:    
                for x in consultaHabilidade:
                    print(x)
        except psycopg2.Error as e:
            print("Erro ao executar a consulta:", e)
        finally:
            cursor.close() 
            
    def deletarHabilidade(self, IDhabilidade:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Delete from habilidade where IDhabilidade = {IDhabilidade};""")
            conexao.commit()
        except psycopg2.Error as e:
            print("Erro ao deletar a Habilidade ", e )
        finally:
            cursor.close()    
                
fogo = Habilidade()
fogo.inserirHabilidade(3,'Fogo',0,100)
fogo.consultarHabildade()    
print("\n")               
fogo.deletarHabilidade(3)
fogo.consultarHabilidadeID(3)