from django.contrib import admin
from .models import DataBaseType, DataBaseConnectionModel, DataSourceModel, DataSourceType



admin.site.register(DataBaseType)
admin.site.register(DataBaseConnectionModel)
admin.site.register(DataSourceModel)
admin.site.register(DataSourceType)

# @admin.register(DataBaseType)
# class PostAdmin(admin.ModelAdmin,):
# 	list_display = ('user', 'slug', 'updated', 'category2')
# 	search_fields = ('slug', 'body2', )
# 	list_filter = ('updated', 'category2')
# 	# prepopulated_fields = {'slug':('body2',)}
# 	raw_id_fields = ('user',)