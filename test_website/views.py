from django.shortcuts import render
from django.views.generic import TemplateView,CreateView



class Home(TemplateView):
    template_name = 'home.html'