from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Pessoa
# Create your views here.

def home(request):
    return HttpResponse('Olá')