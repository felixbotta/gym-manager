from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def home(request):
    template_name = 'home.html'
    return render(request, template_name)
