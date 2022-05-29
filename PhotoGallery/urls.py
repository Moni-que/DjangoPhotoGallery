from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    re_path(r'^$',views.all_photos,name='gallery'),
    re_path(r'^details/(\d{4}-\d{2}-\d{2})/$',views.photo_details,name='photo_details'),
    re_path(r'^search/',views.search_results,name='search_results'),
    re_path(r'^add/',views.add_photo,name='add'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)