from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Dress


# Create your views here.


class DressList(ListView):
    model = Dress
    template_name = 'dress.html'


class DressDetailView(DetailView):
    model = Dress
    context_object_name = 'dresslist'
    template_name = 'dressdetail.html'
