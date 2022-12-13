# -*- coding: utf-8 -*-
# -*- coding: cp1252 -*-
# import webdriver
from __future__ import unicode_literals
import time
from selenium.webdriver.support.select import Select
import pyautogui
from exception.lancar_excecao import lancamento_excecao, lancamento_excecao_telas
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By

PASTA_RELATORIO_CONTRATADOS = r'C:\ISS\relatorio_contratados'
PASTA_LIVRO_PRESTADOS = r'C:\ISS\livro_prestados'
# PASTA_RELATORIO_CONTRATADOS = r'C:\ISS\relatorio_contratados'
# PASTA_LIVRO_PRESTADOS = r'C:\ISS\livro_prestados'


def inserir_IE(driver, IE):
    driver.find_element(By.XPATH, '//*[@id="txtCae"]').send_keys(IE)


def clicar_botao_procurar_empresa(driver):
    driver.find_element(By.CLASS_NAME, 'nc-search').click()


def seleciona_empresa(driver, IE):
    lancamento_excecao(inserir_IE, driver, IE)
    lancamento_excecao(clicar_botao_procurar_empresa, driver)


def menu_toggle(driver):
    driver.find_element(By.XPATH, '//*[@id="menu-toggle"]').click()


def mudar_barra_lateral(driver):
    for _ in range(10):
        try:
            elemento = driver.find_element(By.ID, 'wrapper')
            break
        except ElementNotInteractableException as e:
            print('Retry in 1 second', e)
            time.sleep(1)

    if elemento.get_attribute("class") != 'toggled':
        lancamento_excecao(menu_toggle, driver)


def seleciona_menu(driver):
    lancamento_excecao(mudar_barra_lateral, driver)


def seleciona_menu_contratados_1(driver):
    driver.find_element(By.XPATH, 
        '//*[@id="Menu1_MenuPrincipal"]/ul/li[3]/div/span[3]').click()


def seleciona_menu_contratados_2(driver):
    driver.find_element(By.XPATH,
        '//*[@id="Menu1_MenuPrincipal"]/ul/li[2]/div/span[3]').click()


def seleciona_servicos_contratados(driver, IE, empresa):
    if empresa[6] == 'I':
        lancamento_excecao(seleciona_menu_contratados_1, driver)

    else:
        lancamento_excecao(seleciona_menu_contratados_2, driver)


def consulta_menu_1(driver):
    driver.find_element(By.XPATH, 
        '//*[@id="Menu1_MenuPrincipal"]/ul/li[3]/ul/li[4]/div/a').click()


def consulta_menu_2(driver):
    driver.find_element(By.XPATH,
        '//*[@id="Menu1_MenuPrincipal"]/ul/li[3]/ul/li[6]/div/a').click()


def consulta_menu_3(driver):
    driver.find_element(By.XPATH,
        '//*[@id="Menu1_MenuPrincipal"]/ul/li[2]/ul/li[6]/div/a').click()


def consulta_de_notas_tomadas(driver, simples, empresa):
    if not simples and empresa[6] == 'I':

        lancamento_excecao(consulta_menu_1, driver)

    elif simples and empresa[6] == 'I':

        lancamento_excecao(consulta_menu_2, driver)
    else:

        lancamento_excecao(consulta_menu_3, driver)


# mudar_frame
def switch_frame(driver):
    frame = driver.find_element(By.XPATH, 
        '//*[@id="iframe"]')
    driver.switch_to.frame(frame)


def mudar_frame(driver):
    lancamento_excecao(switch_frame, driver)


def switch_relatorio(driver):
    frame = driver.find_element(By.XPATH,
        '//*[@id="viewer"]')
    driver.switch_to.frame(frame)


def mudar_para_relatorio(driver):
    lancamento_excecao(switch_relatorio, driver)


def frame_principal(driver):
    driver.switch_to.default_content()


def mudar_frame_principal(driver):
    lancamento_excecao(frame_principal, driver)


def clicar_na_serie_nota(driver):
    select = Select(driver.find_element(By.ID, 'ddlSerie'))
    select.select_by_value('22')


def selecionar_serie_nota(driver):
    lancamento_excecao(clicar_na_serie_nota, driver)


def clicar_filtros_adicionais(driver):
    driver.find_element(By.ID, "imbArrow").click()


def selecionar_filtros_adicionais(driver):
    lancamento_excecao(clicar_filtros_adicionais, driver)


def inserir_data_inicial(driver, dt_inicial):
    driver.find_element(By.XPATH, 
        '//*[@id="txtDtEmissaoIni"]').send_keys(dt_inicial)


def selecionar_data_inicial(driver, dt_inicial):
    lancamento_excecao(inserir_data_inicial, driver, dt_inicial)


def inserir_data_final(driver, dt_final):
    driver.find_element(By.XPATH, 
        '//*[@id="txtDtEmissaoFim"]').send_keys(dt_final)


def selecionar_data_final(driver, dt_final):
    lancamento_excecao(inserir_data_final, driver, dt_final)


def clicar_buscar_notas(driver):
    driver.find_element(By.XPATH,
        '//*[@id="btnBuscarNotas"]/span').click()


def buscar_notas(driver):
    lancamento_excecao(clicar_buscar_notas, driver)


def clica_entrar_empresa(driver):
    driver.find_element(By.XPATH,
        '//*[@id="lblNomeEmpresa"]').click()


def trocar_empresa(driver):
    lancamento_excecao(clica_entrar_empresa, driver)


def clicar_botao_imprimir(driver):
    driver.find_element(By.XPATH,
        '//*[@id="btnImprimir"]/span').click()


def carregar_tela_impressao():
    return pyautogui.locateOnScreen('reportManager.png')


def carregar_tela_salvar():
    return pyautogui.locateOnScreen('botao_salvar.png')


def gerar_relatorio_contratados(driver, IE, empresa, caminho, padrao,
                                dt_inicial):

    mes = dt_inicial[3:5]
    ano = dt_inicial[6:10]
    nome_salvar = f'{PASTA_RELATORIO_CONTRATADOS}\\{empresa[4]} {mes}{ano}'

    lancamento_excecao(clicar_botao_imprimir, driver)

    lancamento_excecao_telas(carregar_tela_impressao)

    pyautogui.hotkey('ctrl', 's')
    lancamento_excecao_telas(carregar_tela_salvar)
    time.sleep(2)
    pyautogui.write(nome_salvar)
    time.sleep(2)
    # time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    # lancamento_excecao_telas(carregar_tela_impressao)
    pyautogui.hotkey('alt', 'f4')


def percorrer_menus_servicos_contratados_relatorios(driver, IE, dt_inicial,
                                                    dt_final, simples,
                                                    empresa, caminho):

    seleciona_empresa(driver, IE)
    time.sleep(1)
    seleciona_menu(driver)
    time.sleep(1)
    seleciona_servicos_contratados(driver, IE, empresa)
    time.sleep(1)
    consulta_de_notas_tomadas(driver, simples, empresa)
    time.sleep(1)
    mudar_frame(driver)
    time.sleep(1)
    selecionar_serie_nota(driver)
    time.sleep(1)
    selecionar_filtros_adicionais(driver)
    time.sleep(1)
    selecionar_data_inicial(driver, dt_inicial)
    time.sleep(1)
    selecionar_data_final(driver, dt_final)
    time.sleep(1)
    buscar_notas(driver)
    time.sleep(1)
    gerar_relatorio_contratados(
        driver, IE, empresa, caminho, 'LIVRO ISSQN CONTRATADOS', dt_inicial)


def empresa_do_simples(empresa):
    if empresa[5] == 'N':
        return False
    else:
        return True


def exportar_empresas_contratados(driver, dic_empresas, dt_inicial, dt_final):
    caminho = False
    for empresa in dic_empresas.values():
        Identificador = empresa[4]
        simples = empresa_do_simples(empresa)

        percorrer_menus_servicos_contratados_relatorios(driver, Identificador,
                                                        dt_inicial,
                                                        dt_final, simples,
                                                        empresa, caminho)

        caminho = True
        time.sleep(2)
        # gerar segunda empresa em diante
        mudar_frame_principal(driver)
        trocar_empresa(driver)
        print('*' * 50)
        print('*' * 50)
        print(empresa)
        print('*' * 50)
        print('*' * 50)

    print('Finalizando......', end='')
    for _ in range(10):
        print('..............', end='')
        time.sleep(1)
    driver.close()
    driver.quit()
