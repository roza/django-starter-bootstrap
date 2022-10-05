from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
#from django.test import LiveServerTestCase
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import time
import re

class FunctionalTest(StaticLiveServerTestCase):
    #fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.options = Options()
        cls.options.add_argument("--headless")
        cls.browser = webdriver.Firefox(options=cls.options)
        #cls.browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver',options=cls.options)
        print("Webdriver loaded")
        cls.browser.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_can_show_creation_form(self):
        # Alice se rend sur le site localhost:8000/contacts/
        # et compte y trouver une app de gestion des contacts
        # avec un formulaire de création 
        self.browser.get('%s%s' % (self.live_server_url, '/contacts/'))
        self.browser.implicitly_wait(3)
        # Elle remarque que le mot "Contact"
        # figure dans le titre de la page
        self.assertIn('Contact', self.browser.title)
        #self.fail('Test terminé !')

        # Elle peut aussi créer ce contact ...
        # Puis constater qu'il figure bien
        # dans la page qui liste les contacts ...


    def test_can_add_and_del_contact(self):
        '''Test d'ajout et supression d'un contact '''

        # Alice se rend sur la route de création
        # d'un nouveau contact
        print(self.live_server_url)
        self.browser.get(self.live_server_url+'/contacts/')
        self.browser.implicitly_wait(3)
        # Elle crée un nouveau contact appelé  "Al" "Ouette"
        # Ayant pour mail "al@ouette.org"
        # Avec le message "Lorem ipsum dolor sit amet."
        name = self.browser.find_element(By.ID, "id_name")
        firstname = self.browser.find_element(By.ID,"id_firstname")
        message = self.browser.find_element(By.ID, "id_message")
        email = self.browser.find_element(By.ID,"id_email")
        # Elle envoie son nom, prénom
        name.send_keys("Ouette")
        self.browser.implicitly_wait(1)
        firstname.send_keys("Al")
        self.browser.implicitly_wait(1)
        # puis son email
        email.send_keys("al@ouette.org")
        self.browser.implicitly_wait(1)
        ## Elle crée un message
        message.send_keys("Lorem ipsum dolor sit amet ...")
        self.browser.implicitly_wait(1)

        ## Alice valide le formulaire
        #submit = WebDriverWait(self.browser, 20).until(
        #EC.presence_of_element_located((By.ID, "submit"))).click()
        #submit.click()
        self.browser.find_element(By.ID,"submit").click()
        self.browser.implicitly_wait(5)

        #Le contact doit à présent être créé si tout s'est bien passé
        # Ajuster à votre CSS
        
        title = self.browser.find_element(By.CSS_SELECTOR, ".jumbotron > h2:nth-child(1)")
        self.browser.implicitly_wait(1)
        contactFound = "Ouette" in title.text

        #on vérifie si le contact a bien été trouvé
        self.assertEqual(True,contactFound)

        #à présent Alice va cliquer pour afficher les détails du contact
        #elem.click()
        self.browser.implicitly_wait(1)
        #Puis sélectionner l'icone de suppression pour supprimer le contact
        # Ajuster à votre CSS
        #self.browser.find_elements_by_css_selector("body > div > section.content-header > a:nth-child(1) > i")[0].click()
        

        #on verifie que le contact est bien supprimé
        # Ajuster à votre CSS
        #noms = self.browser.find_elements_by_css_selector("body  > div > section.content-header > div > div > div.box-header > a > h4")
        #contactFound = False
        #for nom in noms:
        #    if re.match("Ouette", nom.text):
        #        contactFound = True
        #self.assertEqual(False,contactFound)
