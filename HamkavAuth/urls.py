from django.urls import path
from . import views
from ninja import NinjaAPI
from rest_framework_simplejwt import views as jwt_views

app_name = 'HamkavAuth'

api = NinjaAPI()     # django-ninja
@api.get("/add")
def add(request, a:int , b:int):
    return {"result": a+b}



urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name = 'user_register' ),
    path('login/', views.UserLoginView.as_view(), name = 'user_login' ),
    path('logout/', views.UserLogoutView.as_view(), name = 'user_logout' ),
    path('passwordecovery/', views.UserPasswordRecoveryView.as_view(), name = 'user_password_recovery' ),
    path('changepassbyrecovery/', views.UserChangePassword.as_view(), name = 'user_change_password_by_recovery' ),
    path('verify/', views.UserRegisterVerifyCodeView.as_view(), name = 'verify_code' ),
    
    path('profile/<int:user_id>/', views.UserProfileView.as_view(), name='user_profile'),
    path('edit_user/', views.EditUserView.as_view(), name='edit_user'),
    path('home/', views.HomeView.as_view(), name = 'home' ),
    
    
    
    # django-ninja
    # path("api/", api.urls),
    
    # rest framework
    path('api/testauth', views.TestAuthView.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
]


