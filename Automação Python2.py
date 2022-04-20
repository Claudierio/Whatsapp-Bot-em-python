import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib

contatos_df = pd.read_excel("Enviar2.xlsx")
print(contatos_df)

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

#espera aparecer o elemento que tem "id" de "side"
while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

#Já estamos com o login no whatsapp web
for i, mensagem in enumerate(contatos_df['Mensagem']): #Para cada msg dentro da coluna de msgs da nossa tabela
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"{mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(5)

    navegador.find_element(By.XPATH,"//span[@data-icon='send']").click()
    time.sleep(8)