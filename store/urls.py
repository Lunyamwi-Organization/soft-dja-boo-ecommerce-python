'''
from django.urls import path, include
from django.conf.urls import url
from .import views as store_views
urlpatterns = [
    path(('home/'),store_views.home,name='home'),
    path(('about/'),store_views.about,name='about'),
]
'''