from selenium.webdriver import Chrome
from pprint import pprint
from time import sleep

'''
# Pegar todos os links de aula
    {'nome da aula':'link da aula'}
# Navegar até o exercício 3
    Achar a url do exercício 3 e ir até lá

'''

browser = Chrome()

browser.get('https://selenium.dunossauro.live/aula_04.html')

def get_links(browser, elemento): # Dicionario
    '''
    Pegar todos os links dentro de um elento
    - Browser = a instância do navegador
    - elemento = webelent[aside, main, body, ul, ol]
    
    '''
    resultado={}
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')
    for ancora in ancoras:
        resultado[ancora.text] =  ancora.get_attribute('href')
        
    return resultado

'''
#Parte 1
'''

sleep(2)

# aside = browser.find_element_by_tag_name('aside')
# aside_ancora = aside.find_elements_by_tag_name('a')
# resultado1 = {}
# for ancora in aside_ancora:
#     resultado1[ancora.text] =  ancora.get_attribute('href')
    
# pprint(resultado1)



#browser.get(resultado1['Aula 3'])
aulas = get_links(browser,'aside')
pprint(aulas)

'''
#Parte 2
'''
exercicios = get_links(browser, 'main')
browser.get(exercicios['Exercício 3'])