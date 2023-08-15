from django.contrib import admin
from .models import ContactModel
 
@admin.register(ContactModel)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['full_name', 'email']
  
  
  
  