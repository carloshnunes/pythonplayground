from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('study-django/', views.study_django, name='study_django'),
    path('create-project/', views.create_project, name='create_project'),
    path('learn-templates/', views.learn_templates, name='learn_templates'),
]
