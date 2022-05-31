from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Category, Image

# Create your views here.

def all_photos(request):
    category = request.GET.get('category')
    if category == None:
        photos = Image.objects.all()
    else:
        photos = Image.objects.filter(image_category__name= category)
    date = dt.date.today()
    categories = Category.objects.all()
    context = { 'categories':  categories, 'photos': photos, 'date': date} 
    return render(request, 'all_images/gallery.html', context)

def photo_details(request):
    photo = Image.objects.get(id=pk)
    return render(request, 'all_images/photo.html', {'photo': photo})


def search_results(request):
    return render(request, 'all_images/search.html')


def add_photo(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['new_category'] != '':
            category, created = Category.objects.get_or_create(none=data['new_category'])
        else:
             category = None
        photo = Image.objects.create(category = category, description = data['image_description'], image =image)

        return redirect('gallery')
    context = { 'categories':  categories}
    return render(request, 'all_images/add.html', context)


