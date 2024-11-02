from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui

# 1 Entrar no Site "https://precos-de-produtos.nnetlify.app/"
driver = webdriver.Chrome()
driver.get('https://precos-de-produtos.nnetlify.app')
sleep(5)

# 2.1 Rolar a página inteira para baixo (e carregar os produtos)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# 2.2 Clicar em "Carregar Mais" Para Vizualizar os produtos restantes
botao_carregar_mais = driver.find_element(By.XPATH, "//button[@id='loadMoreButton']")
sleep(3)
botao_carregar_mais.click()
sleep(3)

# 3 Rolar a página totalmennte para baixo
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(1)

# 4 Subir para o topo da página
driver.execute_script('window.scrollTo(0, 0);')
sleep(2)

# 5 Clicar emm Subir plannilha de preços
botao_carregar_planilha_de_produtos = driver.find_element(By.XPATH,"//button[@class='btn btn-primary btn-custom']")
sleep(2)
botao_carregar_planilha_de_produtos.click()
sleep(5)

# 6 Carregar planilha "precos_produtos-atualizado.xlsx"
pyautogui.write(r'C:\Users\lecem\Downloads\precos-produtos-atualizados.xlsx')
pyautogui.press('enter')
input('Aperte enter no terminal para fechar o programa')






