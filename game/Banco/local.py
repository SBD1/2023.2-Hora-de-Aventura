import psycopg2
from database import Database
from mundo import mundo
from regiao import regiao
class local :
    def __init__(self):
        self.db = Database()
    pass

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
Mundo = mundo()
Mundo.consultarMundo()
Regiao = regiao()
Regiao.consultarRegiao()
Local = local()
Local.consultarLocal() 

 
