from django.shortcuts import render
from django.urls import reverse
from .models import Topic
from .forms import TopicForm, EntryForm 
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'study_register/index.html')


def topics(request):
    """Mostra todos os temas de resumos."""
    # Pega os tópicos contidos no banco de dados
    topics = Topic.objects.order_by('date_added') 
    # Dicionário contendo os tópicos que foram obtidos do banco de dados
    context = {'topics': topics} 
    return render(request,'study_register/topics.html', context)


def topic(request, topic_id):
    """Mostra os resumos de um tema escolhido."""
    # Pega o tópico escolhido utilizando o id passado na requisição
    topic = Topic.objects.get(id = topic_id) 
    # Pega as entradas do tópico por data de inserção
    entries = topic.entry_set.order_by('-date_added') 
    # Dicionário com o tópico e as entradas
    context = {'topic': topic, 'entries': entries} 
    # Retorna o tópico e as anotações para página 'topic'
    return render(request, 'study_register/topic.html', context) 


def new_topic(request):
    """Registra um novo tópico de resumo."""
    if request.method != 'POST':
        # Nenhum dado enviado, cria um formulário em branco.
        form = TopicForm()
    else:
        # Dados enviados, vai processar os dados.

        # Formulário com os dados passados pelo usuário.
        form = TopicForm(request.POST) 
        # Verifica se os dados passados são válidos.
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect(reverse('topics'))
        
    context = {'form': form}
    return render (request, 'study_register/new_topic.html', context)


def new_entry(request, topic_id):
    """Registra uma nova entrada"""
    # Pega o tópico que receberá a nova entrada
    topic = Topic.objects.get(id = topic_id)

    if request.method != 'POST':
        # Nenhum dado enviado, cria um formulário em branco.
        form = EntryForm()
    else:
        # Dados enviados, vai processar os dados.

        # Formulário com os dados passados pelo usuário.
        form = EntryForm(request.POST)
        # Verifica se os dados passados são válidos.
        if form.is_valid():
            # Salva os dados do form, mas não envia para o banco de dados.
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
        
    context = {'topic': topic, 'form': form}
    return render (request, 'study_register/new_entry.html', context)





