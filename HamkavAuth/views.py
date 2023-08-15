from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from django.views import View
from .forms import UserRegisterationForm, UserLoginForm, UserPasswordRecoveryForm, UserChangePasswordForm, VerifyCodeForm, EditUserForm
import random 
from HamkavNotifications.notifs import send_opt_code
from .models import OtpCode, User, Relation
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
# from serializers import UserSerializer

# API  start ==============
class TestAuthView(APIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        return Response("authenticated user!",status=status.HTTP_200_OK)
    
# class CreateUserAPIView(APIView):

#     permission_classes = ()
#     def post(self, request):
#         user = request.data
#         serializer = UserSerializer(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# API end ===================




class ProfileView(View):


    def get(self, request):
        return render(request, 'HamkavAuth/profile.html', {})
    
    
    
class HomeView(View):

    def get(self, request):
        return render(request, 'HamkavAuth/home.html', {})
    
    
    
class UserRegisterView(View):
    form_class = UserRegisterationForm
    template_name = 'HamkavAuth/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            
            
            
            otpReturn = otpHandle(form.cleaned_data['phone']) # generate and store otp code in db and send for user
            if not otpReturn: # اگر شماره وارد شده شامل غیر عدد و یا طول کمتر از ۱۱ بود
                messages.warning(request, 'شماره تلفن به شکل صحیح وارد نمایید')
                return render(request,self.template_name,{'form':form})
                
            
            # # generate random code and send to user
            # random_code = random.randint(1000,9999)
            # send_opt_code(form.cleaned_data['phone'], random_code)
            
            # # store generated random code in db
            # OtpCode.objects.create(
            #     phone_number = form.cleaned_data['phone'],
            #     code = random_code 
            #     )
            
            #store recived user data in registeration form in session temprory
            request.session['user_registeration_info'] = {
                'phone_number' : form.cleaned_data['phone'],
                'email' : form.cleaned_data['email'],
                'full_name' : form.cleaned_data['full_name'],
                'password' : form.cleaned_data['password'],
            }
            messages.success(request, 'کد احزار هویت برای شما ارسال شد','success')
            return redirect('HamkavAuth:verify_code')
        return render(request,self.template_name,{'form':form})
    
    
class UserRegisterVerifyCodeView(View):
    form_class = VerifyCodeForm
    
    def get(self, request):
        form = self.form_class
        return render(request, 'HamkavAuth/verify_code.html', {'form':form})

    
    def post(self,request):
        user_session = request.session['user_registeration_info']
        code_instance = OtpCode.objects.get(phone_number = user_session['phone_number']) # get otpcode from db
        form = self.form_class(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            # if recived code == sended code then create new user by session info
            if cd['code'] == code_instance.code:
                User.objects.create_user(
                    user_session['phone_number'],
                    user_session['email'],
                    user_session['full_name'],
                    user_session['password'],
                    
                )
                code_instance.delete() # delete sended code from otpcode table
                messages.success(request, ' ثبت نام شما باموفقیت انجام شد لطفا وارد شوید', 'success')
                return redirect('HamkavAuth:user_login')
                # return HttpResponseRedirect('/')
            else:
                messages.error(request, 'کد وارد شده صحیح نمی باشد','danger')
                return redirect('HamkavAuth:verify_code')
    
        messages.error(request, 'ورودی های خود را کنترل کنید در صورت نیاز با پشتیبانی سایت تماس بگیرید.','danger')
        return redirect('HamkavAuth:verify_code')

                 
class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'HamkavAuth/login.html'
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone_number = cd['phone'], password = cd['password'])
            if user:
                login(request, user)
                messages.success(request, 'خوش آمدید', 'info')
                return HttpResponseRedirect('/')
                # return HttpResponseRedirect('/blog')
            messages.error(request, 'شماره تلفن یا رمز عبور صحیح نمی باشد', 'warning')
        return render(request, self.template_name, {'form':form})
    

class UserPasswordRecoveryView(View):
    form_class = UserPasswordRecoveryForm
    template_name = 'HamkavAuth/password_recovery.html'    

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.filter(phone_number = cd['phone']).exists()
            if user:
                request.session['user_phone_for_recovery'] = {
                'phone_number' : form.cleaned_data['phone'],
                }
                
                # otpHandle(form.cleaned_data['phone']) # generate and store otp code in db and send for user
                otpReturn = otpHandle(form.cleaned_data['phone']) # generate and store otp code in db and send for user
                if not otpReturn: # اگر شماره وارد شده شامل غیر عدد و یا طول کمتر از ۱۱ بود
                    messages.warning(request, 'شماره تلفن به شکل صحیح وارد نمایید')
                    return render(request,self.template_name,{'form':form})
            
                
                messages.success(request, 'کد احزار هویت برای شما ارسال شد','success')
                return redirect('HamkavAuth:user_change_password_by_recovery')
            messages.success(request, 'کاربری با شماره وارد شده یافت نشد','success')
            return redirect('HamkavAuth:user_password_recovery')
        return render(request,self.template_name,{'form':form})
    
    
    
    
                
class UserChangePassword(View):
    form_class =  UserChangePasswordForm
    template_name = 'HamkavAuth/change_password.html'   
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})
        
    def post(self, request):
        user_session = request.session['user_phone_for_recovery']
        # code_instance = OtpCode.objects.get(phone_number = user_session['phone_number'])
        code_instance = OtpCode.objects.filter(phone_number = user_session['phone_number']).last()
        form = self.form_class(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                user = User.objects.get(phone_number = user_session['phone_number'])
                user.set_password(cd['password'])
                user.save()
                code_instance.delete()
                messages.success(request, ' کلمه عبور با موفقیت تغییر یافت  لطفا به سیستم وارد شوید', 'success')
                return redirect('HamkavAuth:user_login')
            
            messages.warning(request, ' کد وارد شده صحیح نمی باشد ', 'danger')
            return redirect('HamkavAuth:user_change_password_by_recovery')
        
        return render(request, self.template_name, {'form':form})

                

        

            
            
            # اینجا باید ابتدا در زمان درخواست کد برای کاربر سشن تعریف شود و شماره کاربر در سشن ذخیره شود
            # سپس در این گام سشن بازیابی گردد و باکد ثبت شده مقایسه گردد
            # اگر برابر بود پسورد جدید دریافت و در دیتابیس ذخیره گردد
            
            # user = authenticate(request, phone_number = cd['phone'], password = cd['password'])
            # if user:
            #     login(request, user)
            #     messages.success(request, 'خوش آمدید', 'info')
            #     return HttpResponseRedirect('/')
            # messages.error(request, 'شماره تلفن یا رمز عبور صحیح نمی باشد', 'warning')
        return render(request, self.template_name, {'form':form})   
       
       
       
class EditUserView(LoginRequiredMixin, View):
	form_class = EditUserForm

	def get(self, request):
		form = self.form_class(instance=request.user.profile, initial={'email':request.user.email})
		return render(request, 'HamkavAuth/edit_profile.html', {'form':form})

	def post(self, request):
		form = self.form_class(request.POST, instance=request.user.profile)
		if form.is_valid():
			form.save()
			request.user.email = form.cleaned_data['email']
			request.user.save()
			messages.success(request, 'profile edited successfully', 'success')
		return redirect('HamkavAuth:user_profile', request.user.id)                  
            
            
class UserLogoutView(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        messages.success(request, 'با موفقیت از سامانه خارج شدید', 'success')
        # return redirect(request,'accounts/login/')
        # return redirect('HamkavAuth:user_change_password_by_recovery')
    
        return HttpResponseRedirect('/accounts/login/')

        
class UserProfileView(LoginRequiredMixin, View):
	def get(self, request, user_id):
		is_following = False
		user = get_object_or_404(User, pk=user_id)
		posts = user.posts.all()
		relation = Relation.objects.filter(from_user=request.user, to_user=user)
		if relation.exists():
			is_following = True
		return render(request, 'HamkavAuth/profile.html', {'user':user, 'posts':posts, 'is_following':is_following})
                
    
def otpHandle(phone):  
    
    if not phone.isdigit()  or len(phone)<11 :
        return False
    
    
    
    # generate random code and send to user
    random_code = random.randint(1000,9999) 
    send_opt_code(phone, random_code)
    
    # store generated random code in db
    OtpCode.objects.create(
        phone_number = phone,
        code = random_code 
        )
    
    return True
    
