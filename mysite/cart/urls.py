from django.urls import path

from .views import cart_add, cart_detail, cart_remove

app_name = 'cart'
urlpatterns = [
    

    path('add/<int:product_id>/',cart_add,name='cart_add'),
    path('detail/',cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/',cart_remove,name='cart_remove'),

]
