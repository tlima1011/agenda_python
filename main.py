import os
import sqlite3
from sqlite3 import Error
import agenda
import menu_principal
import crud
import sys

##Conexao banco
agenda.ConexaoBanco()

opc = '0'
while opc != '6':
    menu_principal.menuPrincipal()
    opc = input("Digite a opção de acesso do contato: ")[0]
    if opc == '1':
        crud.processInsert()
        os.system("cls")
    elif opc == '2':
        crud.idDeletar()
        os.system("cls")
    elif opc == '3':
        crud.procedureToUpdate()
        os.system("cls")
    elif opc == '4':
        crud.entradaConsulta()
        os.system("cls")
    elif opc == '5':
        crud.entradaConsultaId()
        os.system("cls")
    elif opc == '6':
        print('Programa encerrado...')
    else:
        print('Inválido,digite o número de 1 a 6.')

crud.encerrarBanco()





