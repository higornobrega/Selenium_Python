from selenium.webdriver import Chrome
from time import sleep
from urllib.parse import urlparse
  

browser = Chrome()

browser.get('https://selenium.dunossauro.live/aula_04_a.html')

url_parceada = urlparse(browser.current_url)

print(url_parceada)
print(url_parceada.scheme)
print(url_parceada.netloc)
print(url_parceada.path)

