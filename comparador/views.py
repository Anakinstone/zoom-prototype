from django.http import HttpResponse
from django.shortcuts import render
from .scrappers.consolasML import getconsolasML


def index(request):
    return render(request, 'index.html')


def categorias(request):
    return render(request, 'categorias.html')


def ofertasm(request):
    items = getconsolasML()
    ctx = {
        'items_ml': items
    }
    return render(request, 'ofertasm.html', ctx)
