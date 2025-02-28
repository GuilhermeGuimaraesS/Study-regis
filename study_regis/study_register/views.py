from django.shortcuts import render
from .models import Topic

def index(request):
    return render(request, 'study_register/index.html')


def topics(request):
    """Mostra todos os temas de resumos."""
    topics = Topic.objects.order_by('date_added') # Pega os tópicos contidos no banco de dados
    context = {'topics': topics} # Dicionário contendo os tópicos que foram obtidos do banco de dados
    return render(request,'study_register/topics.html', context)


def topic(request, topic_id):
    """Mostra os resumos de um tema escolhido."""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'study_register/topic.html', context)

