
from medianasms import Client
from medianasms import HTTPError, Error, ResponseCode

from HamkavNotifications.models import sms_sent_log
import time
from HamkavAuth.models import User
from celery import shared_task
from celery.result import AsyncResult
import datetime


# sms pattern 1 : پاسخ به تیکت
# sms pattern 2 : تغییر وصعیت تیکت
# sms pattern 3 : ارجاع به گروه

sms_pattern = {
    "1":"742bmfw59fffh69", 
    "2":"9vp3v74jw518yyw",
    "3":"eq3a3biyoemz2pn",
    "4":"x94lhv7f5vjqg2y",
}

site = 'hamkavapp.ir/'
api_key = 'z93jUAoY1Chv6GpCnWacDKSz1EGvTfBxUIbS6XRcg9k='
sms = Client(api_key)





def send_sms_message(ticket_id = None, access_url = None , user = None, name = None, verb = None, status = None, sms_pattern = None, phone_number = None, code = None):
   
    # recipient_number = '98'+user.username[1:]
    if user:
        recipient_number = '98'+user.phone_number[1:]
    else :
        recipient_number = phone_number
        
    pattern = ""
    
    if sms_pattern:
        if sms_pattern == 1:
            pattern = "742bmfw59fffh69"
            pattern_values = {
            "name": name,
            "ticket_id": str(ticket_id),
            "url": site+access_url,
            }
            result = send_sms.delay(verb , user.id, pattern , recipient_number, pattern_values)
            # print(result.get())
            # print(result)
        elif sms_pattern == 2:
            pattern = "9vp3v74jw518yyw"
            pattern_values = {
            "ticket_id": str(ticket_id),
            "status": status,
            "url": site+access_url,
            }
            result = send_sms.delay(verb , user.id, pattern , recipient_number, pattern_values)
            # print(result.get())
            # print(result)
            
            # print(pattern_values)
        
        elif sms_pattern == 3:
            pattern = "eq3a3biyoemz2pn"
            pattern_values = {
            "ticket_id": str(ticket_id),
            "url": site+access_url,
            }
            result = send_sms.delay(verb , user.id, pattern , recipient_number, pattern_values)
            # res = AsyncResult(result)
            # res.ready()
            # print("****--**///")
            # print(result.id)
            # print(result.status)
            # print(result.get())
            # time.sleep(10)
            # print("/////////")
            # print(result.get())
        elif sms_pattern == 4:
            pattern = "x94lhv7f5vjqg2y"
            pattern_values = {
            "code": str(code),
            }
            result = send_sms( pattern = pattern , recipient_number = recipient_number, pattern_values = pattern_values)
            # res = AsyncResult(result)
            # res.ready()
            # print("****--**///")
            # print(result.id)
            # print(result.status)
            # print(result.get())
            # time.sleep(10)
            # print("/////////")
            # print(result.get())
            
        
# @shared_task(name = 'update__info')        
# @shared_task        
def send_sms(verb = None , user_id = None, pattern = None, recipient_number = None, pattern_values = None):
    try:
        message_id = sms.send_pattern(
            pattern,    # pattern code
            "+985000125475",      # originator
            # "+983000505",      # originator
            recipient_number,  # recipient
            pattern_values,  # pattern values
        )
    
        if user_id:
            user = User.objects.get(id = user_id)
        user  = None
        sms_sent_log.objects.create(verb = verb, recipent_user = user, recipient_number = recipient_number,
                                        message_id = message_id, message_cost = None, pattern_code = pattern)
    except Exception as e:
            print("!!! exception acquired !!! ",datetime.datetime.now())
            raise e

    return True         
        
        # sent_status = sms.get_message(message_id)
        # print(type(sent_status.state),sent_status.state)       # get message status
        # print(type(sent_status.cost),sent_status.cost)        # get message cost
        # print(type(sent_status.return_cost),sent_status.return_cost) # get message payback
    # # site = 'hamkavapp.ir/'
    # # # print('98'+user.username[1:])
   
    # api_key = 'z93jUAoY1Chv6GpCnWacDKSz1EGvTfBxUIbS6XRcg9k='
    # # # create client instance
    # sms = Client(api_key)
    # # # return float64 type credit amount
    # # # credit = sms.get_credit()
    # # # print(create)
    # # recipient_number = '98'+user.username[1:]
    # # message_id = sms.send(
    # #     "+983000505",          # originator
    # #     # "+985000125475",          # originator
    # #     # "+9810001",          # originator
    # #     # [user.username],    # recipients
    # #     # ["989158110553"],    # recipients
    # #     [recipient_number],
    # #     "تست",
    # #     # verb+'\n'+'\n'+'\n'+site+ access_url+'\n'+'\n'+'سامانه همکاو'  , # message
    # #     "از طرف وب سرویس"       # is logged
    # # )
    # # sms_sent_log.objects.create(verb = verb, recipent_user = user, recipient_number = recipient_number )
    # # return True
    
   
    
    # site = 'hamkavapp.ir/'
    # # print('98'+user.username[1:])
    # try:
    #     api_key = 'z93jUAoY1Chv6GpCnWacDKSz1EGvTfBxUIbS6XRcg9k='
    #     # create client instance
    #     sms = Client(api_key)
    #     # return float64 type credit amount
    #     # credit = sms.get_credit()
    #     # print(create)
    #     recipient_number = '98'+user.username[1:]
    #     message_id = sms.send(
    #         # "+983000505",          # originator
    #         "+985000125475",          # originator
    #         # "+9810001",          # originator
    #         # [user.username],    # recipients
    #         # ["989158110553"],    # recipients
    #         [recipient_number],
    #         "تست",
    #         # verb+'\n'+'\n'+'\n'+site+ access_url+'\n'+'\n'+'سامانه همکاو'  , # message
    #         "از طرف وب سرویس"       # is logged
    #     )

    #     sms_sent_log.objects.create(verb = verb, recipent_user = user, recipient_number = recipient_number )
    #     return True
    
    # except Error as e:
    #     print(e)
    #     print("An exception occurred in sending sms")
    #     return False
    