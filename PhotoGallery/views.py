from urllib import request
from django.shortcuts import render, redirect
from django.http  import HttpResponse
import datetime as dt

# Create your views here.
# def welcome(request):
#     return HttpResponse('Welcome to the Moringa Tribune')

# def search_results(request):
#     return render(request, 'all-images/search.html')

def all_photos(request):
    return render(request, 'all_images/gallery.html')
