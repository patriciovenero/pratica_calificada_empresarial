from django import views
from django.urls import path

app_name = 'matricula'

urlpatterns = [
    path('', views.index,name='index'),
]
