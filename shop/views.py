from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse('Conact Us Page: Shop')


def tracker(request):
    return HttpResponse('Tracker Page: Shop')


def search(request):
    return HttpResponse('Search Page: Shop')


def productView(request):
    return HttpResponse('ProductView Page: Shop')


def checkout(request):
    return HttpResponse('Checkout Page: Shop')
