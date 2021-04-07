from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Навзвание', max_length=128, blank=True)
    task = models.TextField('Описание', blank=True)

    
    def __str__(self):
        return self.title