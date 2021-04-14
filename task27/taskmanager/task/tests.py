from django.test import TestCase
from .models import Task

class TestTask(TestCase):

    def setUp(self):
        self.test_title = 'Купить молока'
        self.test_task  = 'Две бутылки 3% - го пастеризованного козьего'
        
    def tearDown(self):
        del self.test_title
        del self.test_task


    def test_count_empty(self):
        task = Task.objects.create(title = self.test_title, task = self.test_task)
        self.assertEqual(task.task_count(), 1)