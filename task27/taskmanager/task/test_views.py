from django.test import TestCase, Client
from .models import Task

class TestTask(TestCase):

    def setUp(self):
        self.test_string = 'Главная'
        self.response = self.client.get('/')
        
 
    def tearDown(self):
        del self.test_string


    def test_status(self):
        self.assertEqual(self.response.status_code, 200)


    def test_context(self):
        self.assertIn(self.test_string, self.response.content.decode(encoding = 'utf-8'))


    
        
     