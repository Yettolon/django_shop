
from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail

from mysite.settings import EMAIL_HOST
from .utilities import signer
from .models import AdvUser, UserData, Product, SubCategory,  EmailForSub, MainImage, Orderjj
from .forms import ChangeUserForm, RegisterNewUserForm, UserDataForm,  send_for_follow, Oplata
from cart.forms import CartAddProductForm
from cart.cart import Cart

def index(request):

    image = MainImage.objects.filter(in_jobs=True)
    product = Product.objects.filter(available=True)[:20]
    

    context = {'image':image,'product':product}
    
    
    

    return render(request,'main/index.html',context)



class MyLoginView(LoginView):

    template_name = 'main/users/login.html'
    def get_success_url(self):
        return reverse_lazy('bboard:profile')


@login_required
def profile(request):

    bb=UserData.objects.filter(pk=request.user.pk)
    
    context = {'bb':bb}

    return render(request, 'main/users/profile.html',context)

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name='main/index.html'

class ChangeUserView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model = AdvUser
    template_name = 'main/users/change_user.html'
    form_class = ChangeUserForm
    success_url = reverse_lazy('bboard:profile')
    success_message = 'Data Change'
    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)
    def get_object(self,queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

class DropPassword(SuccessMessageMixin, PasswordChangeView):
    template_name = 'main/users/drop_password.html'
    success_url = reverse_lazy('bboard:profile')

class RegisterNewUserView(CreateView):
    model = AdvUser
    template_name = 'main/users/register.html'
    form_class = RegisterNewUserForm
    success_url = reverse_lazy('bboard:register_don')

class RegisterDon(TemplateView):
    template_name = 'main/users/register_don.html'

def user_is_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except:
        return render(request,'main/users/register_bed.html')
    user=get_object_or_404(AdvUser, username=username)
    user.is_activated=True
    user.is_active=True
    xxx=UserData(name=username, indexxx=' ', address=' ', phoneNumber=' ')
    xxx.save()
    user.save()
    return render(request, 'main/users/register_activate.html')
'''Редактирование записи в бд'''
@login_required
def billing_change(request):
    try:
        bb=UserData.objects.get(pk=request.user.pk)
    except UserData.DoesNotExist:
        bb = None

    
    if request.method == 'POST':
        bbf = UserDataForm(request.POST, instance=bb)
        if bbf.is_valid():
            bbf.save()
            return HttpResponseRedirect(reverse('bboard:profile'))
            
    else:
        bbf = UserDataForm(instance=bb)
        context = {'bbf':bbf}
        return render(request,'main/users/billing_change.html',context)




def shop_detail(request,slug):
    product = get_object_or_404(Product,  slug=slug, available=True)
    ais = product.additionalimage_set.all()
    cart_product_form = CartAddProductForm()
    context = {'product':product, 'ais':ais, 'cart_product_form':cart_product_form}
    return render(request,'main/single-product.html',context)

@login_required
def checkout(request):
    try:
        bb=UserData.objects.get(pk=request.user.pk)
    except UserData.DoesNotExist:
        bb = None




    
        
    if request.method == 'POST':
        bbf = UserDataForm(request.POST, instance=bb)

        cart = Cart(request)    
        
        if bbf.is_valid():
            bbf.save()
            xx = Orderjj.objects.create(name=bb.name, phoneNumber=bb.phoneNumber,address=bb.address,indexxx=bb.indexxx,total=cart.get_total_price())
            cart.clear()
            x =request.META.get('HTTP_REFERER')
            return redirect(x)
            
    else:
        cssd = Oplata()
        bbf = UserDataForm(instance=bb)
        context = {'bbf':bbf,'cssd':cssd}
        return render(request, 'main/checkout.html',context)

    
def shop_view(request):
    categories = SubCategory.objects.all()
    product = Product.objects.filter(available=True)
    x = 0

    for i in Product.objects.filter(available=True):  # счетчик выводимых записей
        x+=1
    if "keyword" in request.GET:
        keyword = request.GET['keyword']
        q = Q(name__icontains=keyword) | Q(description__icontains=keyword)
        product = product.filter(q)
    else:
        keyword = ''

    paginator = Paginator(product, 8)

    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'product': page.object_list, 'page':page,'x':x, 'categories':categories}
    return render(request, 'main/shop.html', context)

def shop_view_category(request, pk):
    category = get_object_or_404(SubCategory, pk=pk)
    product = Product.objects.filter(available=True, category=pk )
    categories = SubCategory.objects.all()
    x = 0
    for i in product:  # счетчик выводимых записей
        x+=1
    if "keyword" in request.GET:
        keyword = request.GET['keyword']
        q = Q(name__icontains=keyword) | Q(description__icontains=keyword)
        product = product.filter(q)
    else:
        keyword = ''
    paginator = Paginator(product, 8)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'product': page.object_list, 'page':page,'x':x, 'category':category, 'categories':categories}
    return render(request, 'main/shop_category.html', context)
    

def sendler(request):
    emailfor = EmailForSub.objects.all()
    membersmail = AdvUser.objects.filter(send_messages=True)
    senddd = []
    for i in membersmail:
        senddd.append(i.email)
    for i in emailfor:
        if i.emaill not in senddd:
            senddd.append(i.emaill)


    if request.method == 'POST':
        csc_form = send_for_follow()
        
        hosttt = EMAIL_HOST
        if csc_form.is_valid():
            xx = csc_form.cleaned_data['message_for_fol']
            send_mail('Hust', str(xx),str(hosttt),senddd ,fail_silently=False)
            return redirect('bboard:index')
    else:
        csc_form = send_for_follow()




    context = {'csc_form': csc_form}
    return render(request,'main/users/sendler.html', context)

def about(request):
    return render(request,'main/about.html')