from urllib import request
from django.shortcuts import render, redirect
from django.http  import HttpResponse
import datetime as dt

# Create your views here.

def all_photos(request):
    return render(request, 'all_images/gallery.html')



def photo_details(request):
    date = dt.date.today()
    return render(request, 'all_images/photo.html')


def search_results(request):
    return render(request, 'all_images/search.html')


def add(request):
    return render(request, 'all_images/add.html')