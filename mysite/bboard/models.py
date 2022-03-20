
from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from .utilities import timestapppp

class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='activated?')
    send_messages = models.BooleanField(default=True, verbose_name='Subscribe?')
    
    class Meta(AbstractUser.Meta):
        pass


# Create your models here.


class UserData(models.Model):
    name = models.CharField(max_length=50,default=None, verbose_name='Name')
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True, verbose_name='Phone Number', default=None)
    address = models.CharField(max_length=100,default=None, verbose_name='Address')
    indexxx = models.CharField(max_length=15, verbose_name='Index', default=None)

class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    available = models.BooleanField(default=True, verbose_name='Available')
    slug = models.CharField(max_length=150, db_index=True, unique=True)
    name = models.CharField(max_length=100, db_index=True, verbose_name='Name')
    description = models.TextField(max_length=1200, blank=True, verbose_name='Description')
    information = models.TextField(max_length=1500, default=' ', verbose_name='Informations')
    upload = models.DateTimeField(auto_now=True, verbose_name='upload')
    image = models.ImageField(blank=True, verbose_name='Image', upload_to=timestapppp)
    created_at = models.DateField(auto_now_add=True, verbose_name='Created')
    category = models.ForeignKey('Category',on_delete=models.PROTECT, blank=False, verbose_name='Category')
    sale = models.BooleanField(default=False, verbose_name='Sale?')
    def delete(self, *args, **kwargs):
        for i in self.additionalimage_set.all():
            i.delete()
        super().delete(*args, **kwargs)

    class Meta:
        index_together  = (('id','slug'),)
        verbose_name_plural = 'Products'
        verbose_name = 'Product'
        ordering=['created_at']
    
    def __str__(self):
        return self.name
    
    

class AdditionalImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='P')
    image = models.ImageField(upload_to=timestapppp, verbose_name='Image')

    class Meta:
        verbose_name='AddImage'

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Category', db_index=True, unique=True)
    order = models.SmallIntegerField(default=0, db_index=True, verbose_name='int sort')
    super_category = models.ForeignKey('SuperCategory', on_delete=models.PROTECT,blank=True,null=True, verbose_name='Main Category')
    
    def __str__(self):
        return self.name

class SuperCategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_category__isnull=True)

class SuperCategory(Category):
    objects = SuperCategoryManager()

    def __str__(self):
        return self.name
    
    class Meta:
        proxy = True
        ordering = ('order','name')
        verbose_name = 'Main Category'
        verbose_name_plural='Categories'

class SubCategoryManager(models.Manager):
    def get_queryset(self):  
        return super().get_queryset().filter(super_category__isnull=False)

class SubCategory(Category):
    objects = SubCategoryManager()

    def __str__(self):
        return '%s - %s' % (self.super_category.name, self.name)
    
    class Meta:
        proxy = True
        ordering = ('super_category__order','super_category__name','order','name')
        verbose_name = 'SubCategory'
        verbose_name_plural='SubCategories'


class EmailForSub(models.Model):
    emaill = models.EmailField(verbose_name='Email', unique=True)
    
class MainImage(models.Model):
    title = models.CharField(max_length=40, verbose_name='Title')
    content = models.CharField(max_length=60, verbose_name='Content')
    image = models.ImageField(upload_to = timestapppp, verbose_name='Image', blank=False)
    in_jobs = models.BooleanField(verbose_name='In jobs?', default=True)
    order = models.SmallIntegerField(default=0, db_index=True, verbose_name='int sort',unique=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'MainImage'
        verbose_name = 'MainImage'

class About(models.Model):
    text=models.TextField(default='It`s text', verbose_name='Text',blank=True)
    addres = models.CharField(max_length=60, default=None, verbose_name='Address', blank=True)
    email = models.EmailField(default=None,verbose_name='Email')
    mmm = models.BooleanField(default=False, verbose_name='in?')

class Orderjj(models.Model):
    name = models.CharField(max_length=50,default=None, verbose_name='Name')
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True, verbose_name='Phone Number', default=None)
    address = models.CharField(max_length=100,default=None, verbose_name='Address')
    indexxx = models.CharField(max_length=15, verbose_name='Index', default=None)
    total = models.DecimalField(verbose_name='Total', max_digits=15,decimal_places=2)
    opla = models.BooleanField(verbose_name='In way', default=False)
    opla2 = models.BooleanField(verbose_name='Opla',default=False)
    date = models.DateTimeField(auto_now_add=True,verbose_name='Date')
    class Meta:
        verbose_name_plural = 'Order'
        verbose_name = 'Order'
        ordering = ['opla2','opla','date']