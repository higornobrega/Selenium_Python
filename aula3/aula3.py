from time import time
from selenium.webdriver import Chrome
#from selenium.webdriver import Firefox

import time 

navegador = Chrome()
#navegador = Firefox()
time.sleep(2)
navegador.quit()