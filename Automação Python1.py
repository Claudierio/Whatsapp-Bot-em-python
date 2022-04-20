from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import pyperclip
import time 

navegador = webdriver.Chrome()

#1 Passo: Abrir o navegador/Abrir o Whatsapp Web
navegador.get("https://web.whatsapp.com/")
#2 Passo: Passar pela verificação de segurança 
time.sleep(12)
#3 Passo: Pesquisar o nome da pessoa
navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys("Herlan")
time.sleep(2)
#4 Passo: Clicar na conversa daquela pessoa
pyautogui.click(x=831, y=991)
time.sleep(1)
#5 Passo: Mandar uma mensagem para ela
msg = """
Olá! Tudo bem?  
Eu sou um simples bot de Whatsapp
criado em Python 🤖🤖🦾"""
pyperclip.copy(msg)
pyautogui.hotkey("ctrl", "v")
#6 Passo: Enviar  a msg
pyautogui.press("Enter")
#7 Passo: Fechar o navegador
