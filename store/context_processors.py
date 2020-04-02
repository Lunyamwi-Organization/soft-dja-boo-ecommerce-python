from .models import Category, CartItem, Cart
from .views import _cart_id
#add bagdes in the navigation bar to show number of cart items
def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))#get Cart object
            cart_items = CartItem.objects.all().filter(cart=cart[:1])#get corresponding
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except Cart.DoesNotExist: #no cart item in the current session
            item_count=0
    return dict(item_count=item_count)

def menu_links(request):
    links = Category.objects.all()
    return dict (links = links)