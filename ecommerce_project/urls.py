"""ecommerce_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
#import for serving static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#imports for serving media
from django.conf import settings
from django.conf.urls.static import static

from store import views as store_views

store_patterns =[
    path(('home/'),store_views.homePage,name='home'),
    path('category/<slug:category_slug>',store_views.homePage, name ='products_by_category'),
    path(('category/<slug:category_slug>/<slug:product_slug>'),store_views.productPage,name='product_detail'),
    path(('cart/'),store_views.cartPage,name='cart'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^store/',include(store_patterns)),
]
#for serving static files
urlpatterns += staticfiles_urlpatterns()
#for serving media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
