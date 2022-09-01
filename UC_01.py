import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=service)

navegador.get('https://www.cabanadosol.com.br/delivery/pedidos')

navegador.fullscreen_window()
time.sleep(2)
navegador.find_element(By.NAME,'celular').send_keys('99999999999')
time.sleep(2)
navegador.find_element(By.NAME,'email').send_keys('emailfalso@falso.com')
time.sleep(2)
navegador.find_element(By.XPATH,'//*[@id="pedidos"]/div/div/div[1]/form/button').click()
time.sleep(3)