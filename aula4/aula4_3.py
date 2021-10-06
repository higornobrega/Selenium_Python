from selenium.webdriver import Chrome
from time import sleep

def find_by_text(browser, tag, text):
    """
    # Encontrar o Elemento com o texto 'text'.
    Argumentos:
        - browser : Instancia do browser [firefox, chrome, ...]
        - tag : Tag ondo o texto será procurado
        - texto : Conteúdo que deve está na tag
    """
    elementos = browser.find_elements_by_tag_name(tag) #lista
    
    for elemento in elementos:
        if elemento.text == text:
            return elemento
    

browser = Chrome()

browser.get('https://selenium.dunossauro.live/aula_04_b.html')

caixa_de_texto = ['um', 'dois', 'tres', 'quatro'] 

for texto in caixa_de_texto:
    find_by_text(browser, 'div', texto).click()

for texto in caixa_de_texto:
    browser.back() # Voltar na página
    sleep(1)

for texto in caixa_de_texto:
    browser.forward() # Ir para frente 
    sleep(1)
