from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import English, Ielts

# Create your views here.

class English(ListView):
    model = English

class Ielts(ListView):
    model = Ielts