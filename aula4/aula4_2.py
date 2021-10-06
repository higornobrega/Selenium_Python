from selenium.webdriver import Chrome


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

def find_by_href(browser, link):
    """
    # Encontrar o Elemento 'a' com o link 'link'.
    Argumentos:
        - browser : Instancia do browser [firefox, chrome, ...]
        - link : Link que será procurado em todas as tags 'a'
    """
    elementos = browser.find_elements_by_tag_name('a') #lista
    
    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento
    

browser = Chrome()

browser.get('https://selenium.dunossauro.live/aula_04_a.html')
#elemento_ddg = find_by_text(browser, 'li', 'DuckDuckGo')
elemento_ddg = find_by_href(browser, 'ddg')
print(elemento_ddg.get_attribute('href'))
browser.quit()