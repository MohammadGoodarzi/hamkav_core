from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.sessions.models import Session
from .forms import UserCreationForm,UserChangeForm
from .models import User, OtpCode

@admin.register(OtpCode)
class OtpAdmin(admin.ModelAdmin):
    list_display = ('phone_number','code','created',)

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ('email','phone_number', 'is_admin','is_active')
    list_filter = ('is_admin','is_active')
    readonly_fields = ('id','last_login',)
    
    fieldsets =(
        # (None, {'fields':('email','phone_number', 'full_name')}),
        ('Main', {'fields':('email','phone_number', 'full_name','password')}),
        ('identity',{'fields': ( 'user_uuid',)}),
        ('Permissions',{'fields': ('is_active', 'is_admin', 'last_login','groups','user_permissions')}),
    )
    
    
    add_fieldsets = (
        (None, {'fields':('phone_number','email', 'full_name', 'password1', 'password2')}),
        
    )
    
    search_fields = ('email', 'full_name','phone_number')
    ordering = ('full_name',)
    filter_horizontal = ('groups', 'user_permissions')
    
    
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuser'].disabled = True
        return form



# admin.site.unregister(Group)
admin.site.register(User, UserAdmin)



class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
admin.site.register(Session, SessionAdmin)