from django.shortcuts import render, redirect
from django.http  import HttpResponse
import datetime as dt

# Create your views here.
# def welcome(request):
#     return HttpResponse('Welcome to the Moringa Tribune')

def search_results(request):
    return render(request, 'all-images/search.html')
