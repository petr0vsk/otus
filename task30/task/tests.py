from django.test import TestCase
from .models import Task

class TestTask(TestCase):

    def setUp(self):
        self.test_title = 'Главная'
       
        
    def tearDown(self):
        del self.test_title


    def test_count_empty(self):
        task = Task.objects.create(title = self.test_title)
        self.assertEqual(task.task_count(), 1)
