from django.shortcuts import render

def home(request):
  tasks = ["Estudar Django", "Criar um projeto", "Aprender templates"]
  return render(request, 'home.html', {'tasks': tasks})

def about(request):
    return render(request, 'about.html')