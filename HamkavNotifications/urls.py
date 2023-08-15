from django.urls import path,re_path
from django.contrib import admin
from . import views 
from django.conf.urls import include
from rest_framework.routers import DefaultRouter


# app_name='HamkavNotifications'
# app_name='hamkav_notifications'

router = DefaultRouter()
router.register('api_inbox', views.NotificationListView )
router.register('api_seen', views.NotificationListView )
urlpatterns = [
#  path('',views.inbox,name='url-inbox'),  
 path('inbox',views.inbox,name='url-inbox'),  
#  path('inbox', include(router.urls))
 
]
# urlpatterns+=router.urls



