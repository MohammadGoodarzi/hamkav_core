from django.contrib import admin
# from treebeard.admin import TreeAdmin
# from treebeard.forms import movenodeform_factory

# Register your models here.
from .models import MediaModel,MediaTypeModel


admin.site.register(MediaModel)
admin.site.register(MediaTypeModel)
