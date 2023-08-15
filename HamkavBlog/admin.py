from django.contrib import admin
from .models import Post, Comment, Vote, Category, Category2
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from markdownx.admin import MarkdownxModelAdmin


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin,):
	list_display = ('user', 'slug', 'updated', 'category2')
	search_fields = ('slug', 'body2', )
	list_filter = ('updated', 'category2')
	# prepopulated_fields = {'slug':('body2',)}
	raw_id_fields = ('user',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'post', 'created', 'is_reply')
	raw_id_fields = ('user', 'post', 'reply')



class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Category2)

admin.site.register(Category2, MyAdmin)




admin.site.register(Vote)

admin.site.register(Category)