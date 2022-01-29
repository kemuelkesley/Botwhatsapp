from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys # habilitando o teclado.

# BOOT Versão 2.0 By kemuel kesley.

# Navegar até o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/') # pegar o link do Site
time.sleep(20) # Tempo para scanear o celular no navegador.
# Definir Contatos e grupos e mensagem a ser enviada.
contatos = ['Nome do contato']
mensagem = 'Mensagem para o contato ou grupo.'


def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]') # Pegando o campo.
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato) 
    campo_pesquisa.send_keys(Keys.ENTER)


# Enviar mensagem
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]') # pegando a div no whatsapp web, o eleemntes tem que está no plural
    campo_mensagem[1].click()
    time.sleep(3)    
    campo_mensagem[1].send_keys(mensagem) # escrevendo a mensagem        
    campo_mensagem[1].send_keys(Keys.ENTER) # Apertando ENTER e enviando a mensagem.
        

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
