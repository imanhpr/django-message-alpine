from django.urls import path
from django.views.generic import TemplateView
from .views import random_message

urlpatterns = [
    path('' , TemplateView.as_view(template_name='index.html') , name="index"),
    path('send/' , random_message , name='random_message')
]
