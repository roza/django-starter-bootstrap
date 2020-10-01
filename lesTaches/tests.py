from django.test import TestCase

# Create your tests here.


class StringTest(TestCase):
    '''Test unitaire bidon'''
    def test_concatene(self):
        self.assertEqual("Bon"+"jour", "Bonjour")


from lesTaches.views import accueil
from django.urls import resolve
from django.http.request import HttpRequest

class AccueilPageTest(TestCase):
    '''
    Test unitaire de la page accueil sur la racine du projet
    On vérifie que la méthode accueil() est bien invoquée sur /
    '''
    def test_accueil_url_resolves_to_accueil_view(self):
        found = resolve('/lesTaches/')
        self.assertEqual(found.func, accueil)

    def test_accueil_page_content(self):
        '''
        Test Unitaire pour vérifier si le contenu de la page d'accueil 
        de l'app lesTaches est bien retourné par la view accueil()
        '''
        req = HttpRequest()
        response = accueil(req)
        expected = "Bienvenue ici"
        #expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected)

from django.template.loader import render_to_string


