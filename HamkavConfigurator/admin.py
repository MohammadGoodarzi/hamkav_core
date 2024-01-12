from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

# Register your models here.
from .models import Category, Category_type2,Category_type3
from .models import Attribute,AttributeItems



# admin.site.register(Category)

class MyAdmin_Category(TreeAdmin):
    form = movenodeform_factory(Category)

admin.site.register(Category, MyAdmin_Category)

class MyAdmin_Category_type2(TreeAdmin):
    form = movenodeform_factory(Category_type2)

admin.site.register(Category_type2, MyAdmin_Category_type2)

class MyAdmin_Category_type3(TreeAdmin):
    form = movenodeform_factory(Category_type3)

admin.site.register(Category_type3, MyAdmin_Category_type3)

admin.site.register(Attribute)
admin.site.register(AttributeItems)