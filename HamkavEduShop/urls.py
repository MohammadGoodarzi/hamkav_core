
from django.urls import include, path
from .views import ProfileDashboardView, ProfilePostsView

app_name = 'HamkavEduShop'

urlpatterns = [

    path('profile/dashboard', ProfileDashboardView.as_view(), name='profile_dashboard'),
    path('profile/posts', ProfilePostsView.as_view(), name='profile_posts'),

   
    
    #  path('markdownx/', include('markdownx.urls')), #Django Markdownx


]


