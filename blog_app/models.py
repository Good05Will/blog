from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        '''Возвращает строковое представление модели.'''
        if len(self.title) > 20:
            return f'{self.title[:20]}...'
        else:
            return f'{self.title}'



class Note(models.Model):
    '''Информация изученная пользователем по теме.'''
    post = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Возвращает строковое представление модели.'''
        if len(self.text) > 50:
            return f'{self.text[:50]}...'
        else:
            return f'{self.text}'