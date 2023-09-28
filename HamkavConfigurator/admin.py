from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

# Register your models here.
from .models import Category



# admin.site.register(Category)

class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Category)

admin.site.register(Category, MyAdmin)
