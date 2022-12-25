from django.db import models

class Message(models.Model):
    message = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        '''Adminページに表示する文言を設定する'''
        return self.message