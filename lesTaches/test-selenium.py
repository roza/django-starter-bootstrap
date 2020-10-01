# A mettre dans le fichier tests.py
# de l'app Django
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
#browser = webdriver.Firefox()
browser = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver',options=options)
time.sleep(10)
browser.get('http://www.univ-orleans.fr')
assert 'Université' in browser.title

elem = browser.find_element_by_id('edit-search-api-fulltext')
assert(elem is not None)

browser.quit()