from django.shortcuts import render
from . models import notification
from .serializers import NotificationSerializer
from django.contrib.contenttypes.models import ContentType

from HamkavAuth.models import User as User
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status
from rest_framework import viewsets,permissions
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from django.db.models import Q 
from _GeneralHamkavModules import generalHamkavDateTimeOperations as _gHDO
from HamkavAuth import HamkavAuthPermissionModules as _HAPM
from django.contrib.auth.models import Group

def inbox(request):
    # queryset = notification.objects.all()
    s1 = ContentType.objects.get(model = 'notification')
    s2 = s1.get_all_objects_for_this_type(recipent_object_id = request.user.id)
    # print(s2)
    return render(request, 'inbox.html',{'test':s2})

# class NotificationListView(viewsets.ViewSet):
class NotificationListView(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated)
    queryset = notification.objects.all()
    serializer_class = NotificationSerializer
    http_method_names=['get','post','put','patch']
    
    def get_queryset(self):
        return notification.objects.all()
    
    def update(self,request,*args,**kwargs): 
        if request.data["recipent_user"] == request.User:
        
            obj=super().update(request,*args,**kwargs) # دخیره در دیتابیس اصلی
            instance=self.get_object()
            return obj
        else:
            return Response({'message':'شما اجازه ایجاد تغییر ندارید - notificaton-err-101'},status=status.HTTP_403_FORBIDDEN) 
            
            
    # def list(self, request, *args, **kwargs):    
    #     obj=super().list(request,*args,**kwargs)
    #     return obj



# notify.send(
#     self.from_user,
#     recipient=self.to_user,
#     verb='commented',
#     action_object=self.from_user,
#     url="/learn/ask-a-pro/q/test-question-9/299/",
#     other_content="Hello my 'world'"
# )

