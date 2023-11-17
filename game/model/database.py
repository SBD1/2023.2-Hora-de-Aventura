import psycopg2
from psycopg2 import OperationalError
from mundo import mundo

class Database:
    def Conexao():
        conexao = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres123")
        print(conexao.info)
        print(conexao.status)

    def consultarMundo(self,conexao,  nome):
        cursor = conexao.cursor()
        query = """SELECT nome FROM mundo WHERE(mundo.nome = '%s')""" %(nome)  
        cursor.execute(query)
        nome, mundo_destino = cursor.fetchone() 
        cursor.close()
        return mundo(nome, mundo_destino) 
'''
tentativa de fazer um consulta de mundo não com sucesso
'''          