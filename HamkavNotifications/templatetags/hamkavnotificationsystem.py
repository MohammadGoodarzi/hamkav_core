
#  محتویات این فایل بایستی به ماژول pwr
# وارد شود و محل آن در ماژول ناتیفیکشن اشکال دارد 


# from django import template
# from HamkavNotifications .models import notification
# from ..notifs import notif_list
# from PersonalWorkReport.models import pwr
# from _GeneralHamkavModules.generalHamkavDateTimeOperations import getGeorgianToJalali
# from django.db.models import F

# register = template.Library()

# @register.simple_tag
# def person(id):
#     return pwr.objects.filter(pwr_id = id)
#     # return notification.objects.all()
     
# @register.inclusion_tag('show_template_tags.html')     
# def notifications(user):
#     # notifications =  notification.objects.all() 
#     notification_list = notif_list(user)
    
#     # notification_list = notif_list(user).annotate(test=F('timestamp'))
#     # print(notification_list)
    
#     # for i in notification_list:  # افزودن تاریخ جلالی به دیکشنری
#     #     # print(i.id)
#     #     i.jalalidate = getGeorgianToJalali(i.timestamp)   
   
#     return {'notifications': notification_list}
#     # return {'notifications': notifications}
  
     