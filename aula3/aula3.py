from selenium.webdriver import Chrome
#from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

navegador = Chrome()
#navegador = Firefox()
navegador.get(url)
sleep(3)

a = navegador.find_element_by_tag_name('a')

for click in range(10):
    ps = navegador.find_elements_by_tag_name('p')
    a.click()
    print(f'{ps[-1].text}, {click}')
    print(f'{ps[-1].text == click}')
    print(f'{ps[-1].text == str(click)}')

print(f'{a.text}')

navegador.quit()