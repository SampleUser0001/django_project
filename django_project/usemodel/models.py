from django.db import models

class Message(models.Model):
    message = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        '''Adminページに表示する文言を設定する'''
        return self.message

    @staticmethod
    def get_message_list():
        # TODO DBから取得するように変更する。
        message = Message()
        message.message = 'hogehoge'

        message_list = []
        message_list.append(message)

        return message_list

