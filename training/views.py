from django.shortcuts import render, get_object_or_404
from .models import Template


def home(request):
    return render(request, 'training/home.html')


def training(request):
    return render(request, 'training/training.html')


def exercise(request, ex_id):
    template = get_object_or_404(Template, pk=ex_id)
    return render(request, 'training/test.html', {'template': template})
