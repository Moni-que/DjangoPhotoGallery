from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Category, Image

# Create your views here.

def all_photos(request):
    # date = dt.date.today()
    categories = Category.objects.all()
    context = { 'categories':  categories} 
    return render(request, 'all_images/gallery.html', context)

def photo_details(request):
    return render(request, 'all_images/photo.html')


def search_results(request):
    return render(request, 'all_images/search.html')


def add_photo(request):
    return render(request, 'all_images/add.html')