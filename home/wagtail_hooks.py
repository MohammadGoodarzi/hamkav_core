
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register 
from .models import ContactModel



class ContactModelAdmin(ModelAdmin):
    model = ContactModel 
    base_url_path = 'ContactModel' # customise the URL from default to admin/bookadmin
    menu_label = 'ContactModel'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    # list_display = ("name",)
    # list_filter = ("toppings",)
    # search_fields = ("name",)


modeladmin_register(ContactModelAdmin)


#=============================================================wagtail admin customization

from django.utils.html import format_html
from django.templatetags.static import static

from wagtail import hooks




@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static('hamkav/style.css'))

@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static('hamkav/wagtail-admin.css'))



