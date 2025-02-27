from django.shortcuts import render
from .models import Topic

def index(request):
    return render(request, 'study_register/index.html')


def topics(request):
    """Mostra todos os assuntos"""
    topics = Topic.objects.order_by('date_added') # Pega os tópicos contidos no banco de dados
    context = {'topics': topics} # Dicionário contendo os tópicos que foram obtidos do banco de dados
    return render(request,'study_register/topics.html', context)

