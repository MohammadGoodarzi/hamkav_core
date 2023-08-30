from django.contrib import admin

# Register your models here.
from .models import LayoutModel, ChartModel



admin.site.register(LayoutModel)
admin.site.register(ChartModel)