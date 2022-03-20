
from atexit import register
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import AdvUser, SubCategory, SuperCategory, Product, AdditionalImage,MainImage,About, Orderjj
from .forms import SubCategoryForm,ProductCategoryForm

class UsersAdmin(admin.ModelAdmin):
    list_display = ('username','email', 'is_active', 'phoneNumber')
    list_display_links = ('username',)
    list_editable = ('is_active',)
    ordering = ['is_active','username']
    search_fields = ('username', 'phoneNumber','email')
    list_per_page = 40

admin.site.register(AdvUser)
# Register your models here.

class SubCategoryinline(admin.TabularInline):
    model = SubCategory
class SuperCategoryAdmin(admin.ModelAdmin):
    exclude = ('super_category',)
    inlines = (SubCategoryinline,)
admin.site.register(SuperCategory,SuperCategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    form = SubCategoryForm
admin.site.register(SubCategory,SubCategoryAdmin)

class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','imageee','categoryyy','sale','created_at')
    def categoryyy(self,obj):
        return '%s - %s' % (obj.category.super_category.name, obj.category.name)
    categoryyy.short_description = 'Category'
    form = ProductCategoryForm
    


    list_display_links = ('name','imageee')
    def imageee(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60'/>".format(obj.image.url))
        return "None"
    imageee.short_description = "Image"
    ordering = ['created_at',]
    inlines = (AdditionalImageInline,)
    search_fields = ('name',)
    list_per_page = 50

admin.site.register(Product,ProductAdmin)

@admin.register(MainImage)
class MainImageAdmin(admin.ModelAdmin):
    list_per_page = 20

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display =('email','mmm')
    list_per_page = 2

@admin.register(Orderjj)
class AdminOrder(admin.ModelAdmin):
    list_display =('name','opla','opla2','date','total')
    list_per_page = 20