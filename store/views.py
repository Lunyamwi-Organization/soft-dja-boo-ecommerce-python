from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Category, Product 
# Create your views here.
def homePage(request, category_slug=None):
    category_page = None
    products =None
    #i would want to access all my products using their slug
    if category_slug !=None:
        category_page = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category= category_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request,'home.html',{'category': category_page, 'products': products})

def productPage(request, category_slug,product_slug):
    #get our products in a try block
    try:
        product = Product.objects.get(category__slug = category_slug, slug = product_slug)
        # the underscore allows me to access the category slugField model (category.slug)
    except Exception as e:
        raise e
    return render(request,'product.html', {'product': product})

def cartPage(request):
    return render(request, 'cart.html')