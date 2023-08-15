from django.contrib.contenttypes.models import ContentType
from . models import notification
# from PersonalWorkReport.models import pwr
from django.contrib.auth.models import Group, User
from HamkavAuth.models import User
# import tasks as sms_message
from . tasks import send_sms_message 
from . models import sms_policy
# from PersonalWorkReport.models import AppSetting


def send_opt_code(phone_number, code):
    send_sms_message(phone_number = phone_number, code=code, sms_pattern= 4)
        
 
def create(actor,sender,recipent_group = None,recipent_user = None,verb = None,access_url=None,level=None,descripton=None,
            email = 0, sms = 0, push = 0, panel = 1, ticket_id = None, name = None, status = None, sms_pattern = None):
    
    # print(actor)
    # print(sms_pattern)
    # print(ticket_id)
    obj = notification.objects.create(
            actor_content_object = actor, 
            sender_content_object = sender,
            access_url = access_url, 
            recipent_group = recipent_group,
            recipent_user = recipent_user,
            verb = verb ,   
            sms = sms,        # 0 : not set    # 1: must be send   # 2: its sended
            email = email,    # 0 : not set    # 1: must be send   # 2: its sended
            push = push,      # 0 : not set    # 1: must be send   # 2: its sended
            panel = panel     # 0 : not set    # 1: must be send   # 2: its sended
            )
    
    
    try:
        sms_status = sms_policy.objects.values('enable_sending_sms').get()
    except :
        sms_status = False

    if sms_status: 
        if sms_status['enable_sending_sms'] == True:
            
            if recipent_group: # اگر اعلان برای یک گروهی از کاربران ثبت شده بود
                group_users = User.objects.filter(groups__name =recipent_group) # تمام کاربران یک گروه

                for user_ in group_users:
                    result = send_sms_message(
                        ticket_id = ticket_id, name = name , access_url = access_url , user = user_ , verb = verb, status= status, sms_pattern=sms_pattern)

            elif recipent_user:  # اگر اعلان فقط برای یک کاربر ثبت شده بود
                result = send_sms_message(
                    ticket_id = ticket_id, name = name , access_url = access_url , user = recipent_user , verb = verb, status= status, sms_pattern=sms_pattern)
    else:
        print("dont sent sms")
    

def notif_list(recipent):
    
    s1 = ContentType.objects.get(model = 'notification')
    group = recipent.groups.all()

    s2_related_to_user_groups = s1.get_all_objects_for_this_type(recipent_group__in = group).order_by('-id')  # اعلان های گروه هایی که کاربر در آن ها عضو است
    s2_related_to_user = s1.get_all_objects_for_this_type(recipent_user = recipent).order_by('-id') # اعلان های گروه هایی که کاربر در آن ها عضو است
    
    s3 = {"user_notifs":s2_related_to_user ,"user_group_notifs":s2_related_to_user_groups,"count":len(s2_related_to_user)+len(s2_related_to_user_groups)}
#     s3 = s2_related_to_user | s2_related_to_user_groups
    return s3


   
    
    

    