import keyword
from .forms import SearchForm, subscribeee
from cart.cart import Cart
from cart.forms import CartAddProductForm
from .models import SubCategory,About

def bboard_context_processorss(request):
    abouttttt = About.objects.filter(mmm=True)[:1]
    if request.method == 'POST':
        bbbbf = subscribeee(request.POST)
        if bbbbf.is_valid():
            bbbbf.save()
    else:
        bbbbf = subscribeee()    
    
    context = {}
    forrrrrrm = SearchForm()
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                    'update': True})

    categories = SubCategory.objects.all()

    context = {'ssearch': SearchForm(initial={'keyword': keyword}), 'cart':cart ,'forrrrrrm':forrrrrrm,'categories':categories, 'bbbbf':bbbbf,'abouttttt':abouttttt}
    
    return context