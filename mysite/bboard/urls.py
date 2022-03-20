from django.urls import path


from .views import index,  user_is_activate, profile, billing_change, shop_view, shop_detail, checkout, shop_view_category,about,sendler
from .views import MyLoginView, MyLogoutView, ChangeUserView, DropPassword, RegisterDon,RegisterNewUserView

app_name = 'bboard'
urlpatterns = [
    path('about/', about, name='about'),
    path('accounts/profile/billing/', billing_change, name='billing'),
    path('accounts/profile/change/', ChangeUserView.as_view(), name='profile_change'),
    path('accounts/profile/',profile, name='profile'),
    
    path('accounts/register/activate/<str:sign>/', user_is_activate, name='register_activate'),
    path('accounts/register/don', RegisterDon.as_view() ,name='register_don'),
    path('accounts/register/', RegisterNewUserView.as_view() ,name='register'),

    path('accounts/logout/', MyLogoutView.as_view(), name='logout'),
    
    path('accounts/login/', MyLoginView.as_view(), name='login'),
    path('accounts/drop/',DropPassword.as_view(), name='drop'),
    path('accounts/checkout/', checkout, name='checkout'),
    path('sendler/', sendler, name='sendler'),
    path('shop/cat/<int:pk>/', shop_view_category, name='shop_cat'),
    path('shop/<slug:slug>/', shop_detail, name='shop_detail' ),
    path('shop/', shop_view, name='shop_view'),
    path('', index, name='index'),
]

