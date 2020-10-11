from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
#from django.test import LiveServerTestCase
from selenium.webdriver.chrome.options import Options
from time import time
import re

class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.options = Options()
        cls.options.add_argument("--headless")
        #cls.browser = webdriver.Firefox()
        cls.browser = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver',options=cls.options)
        cls.browser.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_can_show_creation_form(self):
        # Alice se rend sur le site localhost:8000/contacts/
        # et compte y trouver une app de gestion des contacts
        # avec un formulaire de création 
        self.browser.get('http://127.0.0.1:8000/contacts/')

        # Elle remarque que le mot "Contact"
        # figure dans le titre de la page
        self.assertIn('Contact', self.browser.title)
        self.fail('Test terminé !')

        # Elle peut aussi créer ce contact ...
        # Puis constater qu'il figure bien
        # dans la page qui liste les contacts ...


    def test_can_add_and_del_contact(self):
        '''Test d'ajout et supression d'un contact '''

        # Alice se rend sur la route de création
        # d'un nouveau contact
        self.browser.get('http://localhost:8000/contacts/')
        time.sleep(1)
        # Elle crée un nouveau contact appelé  "Al" "Ouette"
        # Ayant pour mail "al@ouette.org"
        # Avec le message "Lorem ipsum dolor sit amet."
        name = self.browser.find_element_by_id("id_name")
        firstname = self.browser.find_element_by_id("id_firstname")
        message = self.browser.find_element_by_id("id_message")
        email = self.browser.find_element_by_id("id_email")
        # Elle envoie son nom, prénom
        name.send_keys("Ouette")
        time.sleep(1)
        firstname.send_keys("Al")
        time.sleep(1)
        # puis son email
        email.send_keys("al@ouette.org")
        time.sleep(1)
        ## Elle crée un message
        message.send_keys("Lorem ipsum dolor sit amet ...")
        time.sleep(1)

        ## Alice valide le formulaire
        self.browser.find_element_by_id("submit").click()
        time.sleep(1)

        #Le contact doit à présent être créé si tout s'est bien passé

        noms = self.browser.find_elements_by_css_selector("body > div > div > section.content-header > div > div > div > div.box-header > a > h4")
        time.sleep(1)
        contactFound = False
        elem = None
        for nom in noms:
            if( re.match("Ouette", nom.text) ):
                contactFound = True
                elem = nom

        #on vérifie si le contact a bien été trouvé
        self.assertEqual(True,contactFound)

        #à présent Alice va cliquer pour afficher les détails du contact
        elem.click()
        time.sleep(1)
        #Puis sélectionner l'icone de suppression pour supprimer le contact
        self.browser.find_elements_by_css_selector("body > div > section.content-header > a:nth-child(1) > i")[0].click()
        time.sleep(1)

        #on verifie que le contact est bien supprimé
        noms = self.browser.find_elements_by_css_selector("body > div > div > section.content-header > div > div > div > div.box-header > a > h4")
        contactFound = False
        for nom in noms:
            if( re.match("Ouette", nom.text) ):
                contactFound = True
        self.assertEqual(False,contactFound)