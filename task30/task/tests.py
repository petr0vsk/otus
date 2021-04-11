from django.test import TestCase
from .models import Task


class TestTask(TestCase):


    def test_count_empty(self):
        task = Task.objects.create(title = "123")
        self.assertEqual(task.task_count(), 1)