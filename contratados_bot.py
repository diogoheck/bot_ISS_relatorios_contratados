# -*- coding: cp1252 -*-
from signal import default_int_handler
from tkinter import E
from login import acesso_issnet as acesso
from banco_dados import dicionario_empresas as de
from exportacao_issnet import export_issnet as ISS
from extrair import extrair_XML as arq_xml
from renomear import renomear_arquivos as rename
from copiar_rede_relatorios import copiar_rede as copiar_rede
from remover_arquivos import remover_todos

# remover_todos(r'C:\ISS\relatorio_contratados\*.*')


def app_geracao_relatorio_contratados():

    with open('R:\Compartilhado\Fiscal\lista_clientes_iss\senha.txt', 'r') as arquivo:
        credenciais = arquivo.readlines()
    
    CPF = credenciais[0].replace('\n', '')
    SENHAS = credenciais[1].replace('\n', '').split()
    SENHAS = [int(senha) for senha in SENHAS]

    dt_inicial = '01/12/2022'
    dt_final = '31/12/2022'
    data_lista = dt_inicial.split('/')
    competencia = data_lista[1] + data_lista[2]

    planilha = de.planilha()
    dic_empresas = de.criar_dicionario_empresas(planilha)

    driver = acesso.criar_conexao(CPF, SENHAS)
    ISS.exportar_empresas_contratados(
        driver, dic_empresas, dt_inicial, dt_final)

    rename.renomear_arquivos_contratados(dic_empresas)

    copiar_rede.contratados(dic_empresas, competencia)

    

     


if __name__ == '__main__':
    
    func = app_geracao_relatorio_contratados()
      
