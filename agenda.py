#Importação de pacotes Python
import sqlite3
from sqlite3 import Error

#Conexão com banco de dados
def ConexaoBanco():
    caminho = 'C:\\Users\\\\agendadb.db'
    con = None
    try:
        con = sqlite3.connect(caminho)

    except Error as er:
        print(er)
    return con

vcon=ConexaoBanco()

### CRIAR TABELA
vsql = """CREATE TABLE tb_contatos(
    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    NOME VARCHAR(50), 
    TELEFONE VARCHAR(15), 
    EMAIL VARCHAR(40) 
    )"""

def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print('Tabela criada')
    except Error as er:
        print(er)


criarTabela(vcon, vsql)
vcon.close()
