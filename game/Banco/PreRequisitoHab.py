import psycopg2 
from .Database import Database


class PreRequisitoHab:
    def __init__(self): 
        self.db = Database() 
        pass
    
    def consultarPreRequisitoHab(self):
        try:    
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM prerequisitohab;")
            consultaHabildade = cursor.fetchall()
            if(consultaHabildade == []):
                print("Não foi possivel consultar Os pre requisitos de habildade")
            else:
                for x in consultaHabildade:
                    print(x)
        except psycopg2.Error as e:
            print("Erro ao consultar Habilidade:", e)
        finally:
            cursor.close()
    
    
    def inserirRequisitoHab(self,IDhabilidade:int, requisito:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Insert into prerequisitohab values({IDhabilidade},{requisito});""")
            insercaoHabilidade = conexao.commit()
            return print("Pre Requisito de habilidade criada com sucesso")
        except psycopg2.Error as e:
            print("Erro ao criar pre requisito", e)
        finally:
            cursor.close()
    
              
    def consultarPreRequisitoHabilidadeID(self,IDhabilidade:int, requisito:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Select * from prerequisitohab where IDhabilidade = {IDhabilidade} and requisito = {requisito};""")
            consultaHabilidade = cursor.fetchall()
            if(consultaHabilidade == []):
                print("Erro ao consultar Pre requisito habilidade por ID")
            else:    
                for x in consultaHabilidade:
                    print(x)
        except psycopg2.Error as e:
            print("Erro ao executar a consulta:", e)
        finally:
            cursor.close() 
            
    def deletarRequisitoHab(self, IDhabilidade:int, requisito:int):
        try:
            conexao = self.db.conexao
            cursor = conexao.cursor()
            cursor.execute(f"""Delete from habilidade where IDhabilidade = {IDhabilidade} and requisito = {requisito};""")
            conexao.commit()
        except psycopg2.Error as e:
            print("Erro ao deletar a Habilidade ", e )
        finally:
            cursor.close()    
