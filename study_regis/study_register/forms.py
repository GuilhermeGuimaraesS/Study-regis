from django import forms
from . models import Topic

# Formulário que vai receber os dados que o usuário vai cadastrar.
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic   
        fields = ['text']
        labels = {'text': ''} # Faz com que o campo de texto do formulário venha vazio.


