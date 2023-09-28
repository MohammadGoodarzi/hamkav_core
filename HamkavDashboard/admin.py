from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

# Register your models here.
from .models import LayoutModel, ChartModel, ChartTypeModel





admin.site.register(LayoutModel)
admin.site.register(ChartModel)
admin.site.register(ChartTypeModel)
# admin.site.register(Category)

# class MyAdmin(TreeAdmin):
#     form = movenodeform_factory(Category)

# admin.site.register(Category, MyAdmin)