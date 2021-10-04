from selenium.webdriver import Chrome

browser = Chrome()

browser.get('https://selenium.dunossauro.live/aula_04_a.html')
lista_nao_ordenada = browser.find_element_by_tag_name('ul')
lis = lista_nao_ordenada.find_elements_by_tag_name('li')
a = lis[0].find_element_by_tag_name('a').text

print(f'lista_nao_ordenada - {lista_nao_ordenada} -- lista_nao_ordenada - {lista_nao_ordenada} -- lis - {lis} -- lis[0].find_elements_by_tag_name(a).text - {a}')

