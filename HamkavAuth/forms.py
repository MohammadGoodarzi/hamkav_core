from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Profile

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput )
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput )

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name')

        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('passwords dont match') 
        
        return cd['password2']

    def save(self, commit= True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1']) # hashing password before save
        if commit:
            user.save()
        return user
    
    
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text = "you can change password using <a href = \"../password/\"> this form </a>    ")
    
    class Meta:
        model = User
        fields = ('email', 'full_name', 'password', 'last_login')


class UserRegisterationForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField(label = 'full name')
    phone = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email = email).exists()
        if user:
            raise ValidationError('قبلا توسط این ایمیل ثبت نام انجام گرفته است')
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        user = User.objects.filter(phone_number = phone).exists()
        if user:
            raise ValidationError('قبلا توسط این شماره تلفن ثبت نام صورت گرفته است')
        return phone
    
    
class UserLoginForm(forms.Form):
    phone = forms.CharField(max_length=12)    
    password = forms.CharField(widget=forms.PasswordInput)

    # def clean_phone(self):
    #      phone = self.clean_phone['phone']
    #      user = User.objects.filter(phone_number = phone).exists()
    #      if not user:
    #          raise ValidationError('این شماره در د')


class UserPasswordRecoveryForm(forms.Form):
    phone = forms.CharField(max_length=11)    

    def clean_phone(self):
         phone = self.cleaned_data['phone']
         user = User.objects.filter(phone_number = phone).exists()
         if not user:
             raise ValidationError('شماره وارد شده صحیح نمی باشد میتوانید از منوی ثبت نام اقدام به عضویت نمایید')
         return phone
    
    
class UserChangePasswordForm(forms.Form):
    code = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)    

    # def clean_code(self):
    #      password = self.cleaned_data['password']
    #      user = User.objects.filter(phone_number = phone).exists()
    #      if not user:
    #          raise ValidationError('شماره وارد شده صحیح نمی باشد میتوانید از منوی ثبت نام اقدام به عضویت نمایید')
    #      return phone
     
     
     
    
class EditUserForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = Profile
		fields = ('age', 'bio')     
         
class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()
    