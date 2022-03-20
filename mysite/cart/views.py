from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from bboard.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from bboard.models import UserData
from bboard.forms import UserDataForm


@login_required
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                update_quantity=cd['update'])
    x =request.META.get('HTTP_REFERER')
    return redirect(x)

@login_required
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    x =request.META.get('HTTP_REFERER')
    return redirect(x)

@login_required
def cart_detail(request):
    cart = Cart(request)
    try:
        bb=UserData.objects.get(pk=request.user.pk)
    except UserData.DoesNotExist:
        bb = None


    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                    'update': True})
    
    if request.method == 'POST':
        bbf = UserDataForm(request.POST, instance=bb)
        if bbf.is_valid():
            bbf.save()
            x =request.META.get('HTTP_REFERER')
            return redirect(x)
            
    else:
        bbf = UserDataForm(instance=bb)

    
    context = {'cart': cart ,'bbf':bbf}
    return render(request, 'cart/detail.html', context)
    

    

