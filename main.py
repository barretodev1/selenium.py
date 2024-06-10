import pandas as pd
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

minha_base = pd.read_excel('empresas.xlsx')
print(minha_base)

navegador = webdriver.Chrome()
navegador.get('https://contabilidade-devaprender.netlify.app/')

sleep(2)
email = navegador.find_element(By.XPATH, '//*[@id="email"]').send_keys('caiobarreto1acim@gmail.com')
senha = navegador.find_element(By.XPATH, '//*[@id="senha"]').send_keys('Google20212021@')
enviar = navegador.find_element(By.XPATH, '//*[@id="Entrar"]').click()



for index, row in minha_base.iterrows():
    sleep(3)
    nome_empresa = navegador.find_element(By.XPATH, '//*[@id="nomeEmpresa"]')
    email_empresa = navegador.find_element(By.XPATH, '//*[@id="emailEmpresa"]')
    telefone_empresa = navegador.find_element(By.XPATH, '//*[@id="telefoneEmpresa"]')
    endereço_empresa = navegador.find_element(By.XPATH, '//*[@id="enderecoEmpresa"]')
    meu_CNPJ = navegador.find_element(By.XPATH, '//*[@id="cnpj"]')
    area_atuação = navegador.find_element(By.XPATH, '//*[@id="areaAtuacao"]')
    número_funcionarios = navegador.find_element(By.XPATH, '//*[@id="numeroFuncionarios"]')
    data_fundação = navegador.find_element(By.XPATH, '//*[@id="dataFundacao"]')
    botão_confirmar = navegador.find_element(By.XPATH, '//*[@id="Cadastrar"]')
    
    nome_empresa.send_keys(row['Nome da Empresa'])
    email_empresa.send_keys(row['Email'])
    telefone_empresa.send_keys(row['Telefone'])
    endereço_empresa.send_keys(row['Endereço'])
    meu_CNPJ.send_keys(row['CNPJ'])
    area_atuação.send_keys(row['Área de Atuação'])
    número_funcionarios.send_keys(row['Quantidade de Funcionários'])
    data_fundação.send_keys(row['Data de Fundação'])

    botão_confirmar.click()
    
    



