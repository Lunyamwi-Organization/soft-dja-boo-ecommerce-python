from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Category, Product, Cart, CartItem 
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
#methods to add products in the cart and update their quantity in the cart view
def _cart_id(request):
    cart = request.session.session_key #persists cart while user browses
    if not cart:
        cart = request.session.create()
    return cart
#guarantee that a product is not added more than once to the cart
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
       cart = Cart.objects.get(cart_id=_cart_id(request)) #check whether cart item is still in session
    except Cart.DoesNotExist: #create one if there is none on the session
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()
    try:# creating a complete table in the CartItem class
       cart_item = CartItem.objects.get(product=product, cart=cart)
       cart_item.quantity += 1
       cart_item.save()
    except CartItem.DoesNotExist: #create a new cart item object from the product and cart objects
        cart_item = CartItem.objects.create(
         #first time the product is added to the cart hence the qty=1
              product = product,
              quantity = 1,
              cart = cart
        ) #call save method to store it then redirect to another url
        cart_item.save()
    return redirect('cart_detail')# name of my url which will then create these items in my current session
#retrieve all cart items in the current session
def cart_detail(request, total=0,counter=0,cart_items=None):
    try:#checks if the cart is present in the session does the pricing
        cart  = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:#not present in session please ignore
        pass
    #it is time to now call my html, passing all the context variables as dictionary
    return render(request, 'cart.html', dict(cart_items = cart_items, total = total, counter = counter))
    


    

'''
def cartPage(request):
    return render(request, 'cart.html')
'''