from django import forms
from . models import Topic, Entry

# Formulário que vai receber o novo tópico que o usuário vai cadastrar.
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic   
        fields = ['text']
        labels = {'text': ''} # Faz com que o campo de texto do formulário venha vazio.

class EntryForm(forms.ModelForm):
    class Meta:
        model= Entry
        fields = ['text']
        labels = {'text': ''}
        # Cria uma área de texto com 80 colunas
        widgets = {'text': forms.Textarea(attrs={'cols': 100})}

