from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from HamkavAuth.models import User
from django.contrib.auth.models import Group

from django.db import models



class notification(models.Model): # notification 
    
    verb =   models.CharField(max_length=200,null=True,blank=True) 
    level =  models.CharField(max_length=10,null=True,blank=True) 
    description =   models.CharField(max_length=500,null=True,blank=True) 
    timestamp =  models.DateTimeField(auto_now_add=True)
    access_url = models.CharField(max_length=500,null=True,blank=True) 

    # actor object::   
    actor_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='notification_actor_content_type')  
    actor_object_id = models.PositiveIntegerField()  
    actor_content_object = GenericForeignKey('actor_content_type', 'actor_object_id')
    
    
    # #sender object :
    sender_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='notification_sender_content_type')  
    sender_object_id = models.PositiveIntegerField()  
    sender_content_object = GenericForeignKey('sender_content_type', 'sender_object_id')
    
    #  #recipent object :
    recipent_user = models.ForeignKey(User, related_name='notification_recipent_user', on_delete=models.CASCADE, null=True)
    recipent_group = models.ForeignKey(Group, related_name='notification_recipent_group', on_delete=models.CASCADE, null=True)

    # recipent_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='notification_recipent_content_type')  
    # recipent_object_id = models.PositiveIntegerField()  
    # recipent_content_object = GenericForeignKey('recipent_content_type', 'recipent_object_id')
    


    # 0 : not set
    # 1: must be send
    # 2: its sended
    
    unread =  models.PositiveSmallIntegerField(default=1)
    public = models.PositiveSmallIntegerField(default=0) 
    
    email =  models.PositiveSmallIntegerField(default=0) 
    sms =  models.PositiveSmallIntegerField(default=0) 
    push =  models.PositiveSmallIntegerField(default=0)   # push notification
    panel =  models.PositiveSmallIntegerField(default=1)   # push notification
    
    deleted =  models.BooleanField(default=False)   # push notification

    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  
    # object_id = models.PositiveIntegerField()  
    # content_object = GenericForeignKey('content_type', 'object_id')
            
    def __str__(self):
        return f'{self.verb}'
  
  
class sms_policy(models.Model):
    enable_sending_sms = models.BooleanField(default=True)
    allowed_sending_users = models.ManyToManyField(User, blank = True)
    allowed_sending_groups = models.ManyToManyField(Group, blank = True)
    
class sms_sent_log(models.Model):
    timestamp =  models.DateTimeField(auto_now_add=True) # زمان ارسال
    verb = models.CharField(max_length=500, null=True, blank=True) # متن ارسالی به مخاطب
    recipent_user = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    recipient_number = models.CharField(max_length=12)
    message_id = models.CharField(max_length=15, null=True, blank=True) # کد پیام ارسالی از پنل
    message_cost = models.FloatField(null=True, blank=True) # کد پیام ارسالی از پنل
    pattern_code = models.CharField(max_length=50, null=True, blank=True)
    # page = models.PositiveSmallIntegerField(null=True, blank=True) # تعداد صحفحات پیام ارسالی
    # sms_provider = models.charField(max_length=50, null=True, blank=True)
    
                
    def __str__(self):
        return f'{self.timestamp}- {self.verb} - {self.recipent_user.first_name} {self.recipent_user.last_name} "{self.recipient_number}" '