from django.shortcuts import render

def index(request):
    return render(request, 'study_register/index.html')

