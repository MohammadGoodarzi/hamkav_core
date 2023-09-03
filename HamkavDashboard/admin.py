from django.contrib import admin

# Register your models here.
from .models import LayoutModel, ChartModel, ChartTypeModel



admin.site.register(LayoutModel)
admin.site.register(ChartModel)
admin.site.register(ChartTypeModel)