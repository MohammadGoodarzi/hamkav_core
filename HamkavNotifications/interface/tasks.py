
# from ippanel import Client
# from ippanel import HTTPError, Error, ResponseCode
# from HamkavNotifications.models import sms_sent_log
# import time
# from celery import shared_task


# # sms pattern 1 : پاسخ به تیکت
# # sms pattern 2 : تغییر وصعیت تیکت
# # sms pattern 3 : ارجاع به گروه

# sms_pattern = {
#     "1":"742bmfw59fffh69", 
#     "2":"9vp3v74jw518yyw",
#     "3":"eq3a3biyoemz2pn",
# }

# site = 'hamkavapp.ir/'
# api_key = 'z93jUAoY1Chv6GpCnWacDKSz1EGvTfBxUIbS6XRcg9k='
# sms = Client(api_key)


# def send_sms_message(ticket_id, access_url , user, name, verb, status, sms_pattern):
#     # recipient_number = '98'+user.username[1:]
#     recipient_number = '98'+user.phone_number[1:]
#     pattern = ""
    
#     if sms_pattern:
#         if sms_pattern == 1:
#             pattern = "742bmfw59fffh69"
#             pattern_values = {
#             "name": name,
#             "ticket_id": str(ticket_id),
#             "url": site+access_url,
#             }
#             result = send_sms.delay(verb , user, pattern , recipient_number, pattern_values)
#             print(result)
#         elif sms_pattern == 2:
#             pattern = "9vp3v74jw518yyw"
#             pattern_values = {
#             "ticket_id": str(ticket_id),
#             "status": status,
#             "url": site+access_url,
#             }
#             result = send_sms.delay(verb , user, pattern , recipient_number, pattern_values)
#             print(result)
            
#             # print(pattern_values)
        
#         elif sms_pattern == 3:
#             pattern = "eq3a3biyoemz2pn"
#             pattern_values = {
#             "ticket_id": str(ticket_id),
#             "url": site+access_url,
#             }
#             result = send_sms.delay(verb , user, pattern , recipient_number, pattern_values)
#             print(result)
            
        
# @shared_task        
# def send_sms(verb , user, pattern = None, recipient_number = None, pattern_values = None):
#     # message_id = sms.send_pattern(
#     #     pattern,    # pattern code
#     #     "+985000125475",      # originator
#     #     # "+983000505",      # originator
#     #     recipient_number,  # recipient
#     #     pattern_values,  # pattern values
#     # )
#     # time.sleep(60)
#     # sms_sent_log.objects.create(verb = verb, recipent_user = user, recipient_number = recipient_number,
#     #                                 message_id = message_id, message_cost = None, pattern_code = pattern)  
#     sms_sent_log.objects.create(verb = verb, recipent_user = user, recipient_number = recipient_number,
#                                     message_id = None, message_cost = None, pattern_code = pattern)   
#     return True         
        
#         # sent_status = sms.get_message(message_id)
#         # print(type(sent_status.state),sent_status.state)       # get message status
#         # print(type(sent_status.cost),sent_status.cost)        # get message cost
#         # print(type(sent_status.return_cost),sent_status.return_cost) # get message payback
#     # # site = 'hamkavapp.ir/'
#     # # # print('98'+user.username[1:])
   
#     # api_key = 'z93jUAoY1Chv6GpCnWacDKSz1EGvTfBxUIbS6XRcg9k='
#     # # # create client instance
#     # sms = Client(api_key)
#     # # # return float64 type credit amount
#     # # # credit = sms.get_credit()
#     # # # print(create)
#     # # recipient_number = '98'+user.username[1:]
#     # # message_id = sms.send(
#     # #     "+983000505",          # originator
#     # #     # "+985000125475",          # originator
#     # #     # "+9810001",          # originator
#     # #     # [user.username],    # recipients
#     # #     # ["989158110553"],    # recipients
#     # #     [recipient_number],
#     # #     "تست",
#     # #     # verb+'\n'+'\n'+'\n'+site+ access_url+'\n'+'\n'+'سامانه همکاو'  , # message
#     # #     "از طرف وب سرویس"       # is logged
#     # # )
#     # # sms_sent_log.objects.create(verb = verb, recipent_user = user, recipient_number = recipient_number )
#     # # return True
    
   
    
#     # site = 'hamkavapp.ir/'
#     # # print('98'+user.username[1:])
#     # try:
#     #     api_key = 'z93jUAoY1Chv6GpCnWacDKSz1EGvTfBxUIbS6XRcg9k='
#     #     # create client instance
#     #     sms = Client(api_key)
#     #     # return float64 type credit amount
#     #     # credit = sms.get_credit()
#     #     # print(create)
#     #     recipient_number = '98'+user.username[1:]
#     #     message_id = sms.send(
#     #         # "+983000505",          # originator
#     #         "+985000125475",          # originator
#     #         # "+9810001",          # originator
#     #         # [user.username],    # recipients
#     #         # ["989158110553"],    # recipients
#     #         [recipient_number],
#     #         "تست",
#     #         # verb+'\n'+'\n'+'\n'+site+ access_url+'\n'+'\n'+'سامانه همکاو'  , # message
#     #         "از طرف وب سرویس"       # is logged
#     #     )

#     #     sms_sent_log.objects.create(verb = verb, recipent_user = user, recipient_number = recipient_number )
#     #     return True
    
#     # except Error as e:
#     #     print(e)
#     #     print("An exception occurred in sending sms")
#     #     return False
    