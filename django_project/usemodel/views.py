from django.shortcuts import render
from .models import Message

def index(request):
    message_list = Message.get_message_list()
    context = {
        'message_list': message_list,
    }
    return render(request, 'usemodel/index.html', context)

def add_message(request):
    return render(request, 'usemodel/add_message.html')
