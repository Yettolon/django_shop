
from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .apps import user_reg
from .models import AdvUser, UserData, SubCategory,SuperCategory,Product, EmailForSub

class ChangeUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='email')

    class Meta:
        model = AdvUser
        fields = ('username','email','send_messages')


class RegisterNewUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput, )
    passwordd = forms.CharField(label='Confirm password',  widget=forms.PasswordInput, )
    username = forms.CharField(label='Username', required=True)
    
    def clean_password1(self):
        password = self.cleaned_data['password']
        if password:
            password_validation.validate_password(password)
        return password
    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        passwordd = self.cleaned_data['passwordd']
        if password and passwordd and passwordd != password:
            errors = {'passwordd': ValidationError('Password don`t match.', code='password_mismatch')}
            raise ValidationError(errors)
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_activated=False
        user.is_active = False
        if commit:
            user.save()
        user_reg.send(RegisterNewUserForm,instance=user)
        return user
    
    class Meta:
        model = AdvUser
        fields = ('username','email','password', 'passwordd', 'send_messages')

class UserDataForm(forms.ModelForm):
    
    
    class Meta:
        model = UserData

    
        fields = ('name','phoneNumber','address','indexxx')

class UserDataForm(forms.ModelForm):
    
    
    class Meta:
        model = UserData

    
        fields = ('name','phoneNumber','address','indexxx')

class SubCategoryForm(forms.ModelForm):
    super_category= forms.ModelChoiceField(queryset=SuperCategory.objects.all(), empty_label=None, label='Category', required=False)

    class Meta:
        model = SubCategory
        fields = '__all__'

class ProductCategoryForm(forms.ModelForm):
    category= forms.ModelChoiceField(queryset=SubCategory.objects.all(), empty_label=None, label='Category', required=True)

    class Meta:
        model = Product
        fields = '__all__'

class SearchForm(forms.Form):
    keyword = forms.CharField(required=False, max_length=40, label='',widget=forms.TextInput(attrs={'placeholder':'search'}))

class send_for_follow(forms.Form):
    message_for_fol = forms.CharField(required=True, max_length=1500,widget=forms.TextInput(attrs={'placeholder':'Message'}) )

class subscribeee(forms.ModelForm):
    emaill = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder':'write'}))
    class Meta:
        model = EmailForSub
        fields = '__all__'

class Oplata(forms.Form):
    cssd = forms.BooleanField(label='buy')