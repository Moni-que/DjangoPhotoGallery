from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
import datetime as dt

# Create your views here.

def all_photos(request):
    date = dt.date.today()
    return render(request, 'all_images/gallery.html', {"date": date})


def photo_details(request,past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(all_photos)

    return render(request, 'all_images/photo.html', {"date": date})


def search_results(request):
    return render(request, 'all_images/search.html')


def add_photo(request):
    return render(request, 'all_images/add.html')