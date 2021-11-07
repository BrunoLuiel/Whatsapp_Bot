from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\ADM\Documents\Python Class\Whatsapp_Boot\chromedriver.exe')
driver.get('https://web.whatsapp.com/')
time.sleep(35)

def busca_contato(contatos):
    pesquisa_contato = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    pesquisa_contato.click()
    time.sleep(1)
    pesquisa_contato.clear()
    pesquisa_contato.send_keys(contatos + Keys.ENTER)
    time.sleep(2)

def envia_mensagem(msg):
        caixa_mensagem = driver.find_element_by_xpath('//*[contains(@class, "copyable-text selectable-text")][@spellcheck="true"]')
        time.sleep(2)
        caixa_mensagem.clear()
        caixa_mensagem.click()
        time.sleep(1)
        caixa_mensagem.send_keys(msg + Keys.ENTER)
        time.sleep(2)


contatos = ["Ammor", "Mamãe", "Tia Wanda", "Luana Maninha"]
msg = "Boa noite e um excelente restinho de sabado pra você <3"
for contato in contatos:
    busca_contato(contato)
    envia_mensagem(msg)