from django.shortcuts import render

def home(request):
    tasks = ["Study Django", "Create a Project", "Learn Templates"]
    return render(request, 'index.html', {'tasks': tasks})

def about(request):
    return render(request, 'about.html')

def study_django(request):
    return render(request, 'study_django.html')

def create_project(request):
    return render(request, 'create_project.html')

def learn_templates(request):
    return render(request, 'learn_templates.html')
