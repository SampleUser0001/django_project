from django import forms
from .model import Message

class AddMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('message', 'pub_date')