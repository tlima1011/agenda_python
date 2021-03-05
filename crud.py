#Importação de pacotes Python
import sqlite3
from sqlite3 import Error
import os
import sys

#Conexão com banco de dados
def ConexaoBanco():
    caminho = 'C:\\Users\\thiag\\Documents\\Projeto Python - BPA Technologies\SQLiteStudio\\agenda\\agendadb.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as er:
        print(er)
    return con

vcon=ConexaoBanco()

#Create
def processInsert():
    nome = input('Digite o nome: ')
    telefone = input('Digite o telefone: ')
    email = input('Digite o e-mail: ')

    sql = "INSERT INTO TB_CONTATOS(NOME, TELEFONE, EMAIL) VALUES('"+nome+"', '"+telefone+ "','"+email+"')"
    try:
        c = vcon.cursor()
        c.execute(sql)
        #inserir(vcon, sql)
        vcon.commit()
        entradaConsulta()
    except Error as er:
        print(er)
    finally:
        print('Registro inserido' )

def entradaConsulta():

    vsql = "SELECT * FROM TB_CONTATOS"
    res = consultarTodos(vcon, vsql)
    for r in res:
        print(r)


def consultarTodos(vcon, vsql):
    sql = "SELECT * FROM TB_CONTATOS"
    c = vcon.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    print('***TABELA DE CONTATOS: ***')
    return resultado

    res = consultarTodos(vcon, sql)
    for r in res:
        print(r)

def entradaConsultaId():
    idConsulta = int(input('Informe o ID para consultar: '))
    sql = "SELECT * FROM TB_CONTATOS WHERE ID = " + str(idConsulta)
    res = consultarPorId(vcon, sql)
    for r in res:
        print(r)

def consultarPorId(vcon, sql):
    c = vcon.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    print('***TABELA DE CONTATOS: ***' )
    return resultado

#Update by ID
def procedureToUpdate():
    id_atualizar = int(input('Informe o #id para atualizar: '))
    novo_nome = str(input('Informe um novo nome: '))
    novo_telefone = str(input('Informe um novo telefone: '))
    novo_email = str(input('Informe um nono email: '))

    vsql = "UPDATE TB_CONTATOS SET NOME='"+novo_nome +"',TELEFONE='" + novo_telefone + "', EMAIL='" +novo_email+ "' WHERE ID =" + str(id_atualizar)
    atualizar(vcon, vsql)


def atualizar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro atualizado' )
    except Error as er:
        print(er)
    finally:
        print("Encerrado procedimento de atualização")


#Delete by ID
def idDeletar():
    id_deletar = int(input('Informe o #id para deletar: '))
    vsql = "DELETE FROM TB_CONTATOS WHERE ID = " + str(id_deletar)
    deletar(vcon, vsql)

def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro excluído' )
    except Error as er:
        print(er)
    finally:
        print("Ecerrado procedimento de exclusão")





