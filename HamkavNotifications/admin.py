from dataclasses import fields
from django.contrib import admin
from HamkavNotifications.models import notification, sms_policy, sms_sent_log
from django.contrib.contenttypes.models import ContentType


# @admin.register(notification)
# class pwrAdmin(admin.ModelAdmin):
#      list_display = ('id','verb')
#     #list_display = [field.name for field in notification._meta.get_fields()]

admin.site.register(notification)
admin.site.register(ContentType)
admin.site.register(sms_policy)
admin.site.register(sms_sent_log)