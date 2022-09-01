import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=service)

navegador.get('https://www.cabanadosol.com.br/delivery')

navegador.fullscreen_window()
time.sleep(2)

#adicionando o primeiro item ao carrinho
navegador.find_element(By.XPATH,'//*[@id="delivery"]/div[1]/main/div[1]/div/button').click()
time.sleep(2)
#adicionando o segundo item ao carrinho
navegador.find_element(By.XPATH,'//*[@id="delivery"]/div[1]/main/div[2]/div/button').click()
time.sleep(2)

#verificando a página do carrinho, para ver se os itens estão salvos
navegador.find_element(By.XPATH,'//*[@id="header"]/div[1]/a[2]').click()
time.sleep(2)

#retirando o primeiro item do carrinho
navegador.find_element(By.XPATH,'//*[@id="carrinho"]/div/div/div/div[1]/div[4]/button[3]').click()
time.sleep(2)

#retirando o segundo item do carrinho
navegador.find_element(By.XPATH,'//*[@id="carrinho"]/div/div/div/div/div[4]/button[3]').click()
time.sleep(2)