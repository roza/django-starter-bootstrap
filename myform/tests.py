from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
#from django.test import LiveServerTestCase
from selenium.webdriver.chrome.options import Options

class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.options = Options()
        cls.options.add_argument("--headless")
        cls.browser = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver',
        options=cls.options)
        cls.browser.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_can_show_task_list(self):
        # Alice se rend sur le site localhost:8000
        # et compte y trouver une app de gestion des contacts
        # sur la route /contacts/
        self.browser.get('http://127.0.0.1:8000/contacts/')

        # Elle remarque que le mot "Contact"
        # figure dans le titre de la page
        self.assertIn('Contact', self.browser.title)
        self.fail('Test terminé !')

        # Elle peut aussi créer une nouvelle tâche ...
        # Puis constater qu'elle figure bien
        # dans la page qui liste les tâches ...


    def test_add_task(self):
        '''Test d'ajout et supression d'un contact '''

        # Alice se rend sur la route de création
        # d'une nouvelle tâche
        browser = webdriver.Chrome()
        browser.get('http://localhost:8000/contacts/')
        time.sleep(1)
        # Elle crée un nouveau contact appelé  "Al" "Ouette"
        # Ayant pour mail "al@ouette.org"
        # Avec le message "Lorem ipsum dolor sit amet."
        name = browser.find_element_by_id("id_name")
        firstname = browser.find_element_by_id("id_firstname")
        message = browser.find_element_by_id("id_message")
        email = browser.find_element_by_id("id_email")
        # Elle envoie son nom, prénom
        name.send_keys("Ouette")
        time.sleep(1)
        firstname.send_keys("Al")
        time.sleep(1)
        # puis son email
        email.send_keys("al@ouette.org")
        time.sleep(1)
        ## Elle crée un message
        message.send_keys("Lorem ipsum dolor sit amet.")
        time.sleep(1)

        ## Alice valide le formulaire
        browser.find_element_by_id("submit").click()
        time.sleep(1)

        #La tache doit à présent être créée si tout s'est bien passé

        noms = browser.find_elements_by_css_selector("body > div > div > section.content-header > div > div > div > div.box-header > a > h4")
        time.sleep(1)
        taskFound = False
        elem = None
        for nom in noms:
            if( re.match("Ma superbe tache", nom.text) ):
                taskFound = True
                elem = nom

        #on vérifie si la tache est crée
        self.assertEqual(True,taskFound)

        #à présent Alice va cliquer pour afficher la tâche
        elem.click()
        time.sleep(1)
        #Puis sélectionner l'icone de suppression pour supprimer la tâche
        browser.find_elements_by_css_selector("body > div > section.content-header > a:nth-child(1) > i")[0].click()
        time.sleep(1)

        #on verifie que la tâche est supprimée
        noms = browser.find_elements_by_css_selector("body > div > div > section.content-header > div > div > div > div.box-header > a > h4")
        taskFound = False
        for nom in noms:
            if( re.match("Ma super tache", nom.text) ):
                taskFound = True

        browser.quit()