from .wagtail_models import *
from .wagtail_forms import *

# Create your models here.
from django.db import models
from HamkavAuth.models import User
from django.urls import reverse
# from wagtail.fields import RichTextField
from markdownx.models import MarkdownxField
from django.utils.text import slugify

import re

from treebeard.mp_tree import MP_Node
import locale
import jdatetime
from taggit.managers import TaggableManager


class Category2(MP_Node):
    name = models.CharField(max_length=30)

    node_order_by = ['name']

    def __str__(self):
        return '{}'.format(self.name)


class Category(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_category')
	slug = models.SlugField(null=False, blank=False)
	name = models.CharField(max_length=100, null=True, blank=True)
	label = models.CharField(max_length=100, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
 
	def __str__(self):
		return f'{self.slug} - {self.label} - {self.user}'

	def get_absolute_url(self):
		return reverse("HamkavBlog:category_detail", args=(self.id, self.slug))
	



class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	category = models.ForeignKey(Category,null=True, on_delete=models.CASCADE, related_name='category_post')
	category2 = models.ForeignKey(Category2,null=True, on_delete=models.CASCADE, related_name='category2_post')
	# body2 =   MarkdownxField(null=True)
	body = models.TextField(null=True)
	brife = models.CharField(max_length=300, null=True, blank=True)
	slug = models.SlugField(null=False, blank=False, editable=False)
	title = models.CharField(max_length=100) 
	tags = TaggableManager()
	is_published = models.BooleanField(default=True) # آيا این پست منتشر شده است یاتنها ذخیره شده
	is_restricted = models.BooleanField(default=False) # آیا دسترسی خاصی برای این مقاله تعیین شده است؟
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	created_shamsi = models.CharField(max_length=50, null=True, editable=False)
	updated_shamsi = models.CharField(max_length=50, null=True, editable=False)
	is_deleted = models.BooleanField(null=True)
	

	class Meta:
		ordering = ['-created']
  
	def __str__(self):
		return f'{self.slug} - {self.updated} - {self.user}'

	def get_absolute_url(self):
		return reverse('HamkavBlog:post_detail', args=(self.id, self.slug))

	def likes_count(self):
		return self.pvotes.count()

	def user_can_like(self, user):
		user_like = user.uvotes.filter(post=self)
		if user_like.exists():
			return True
		return False
    
	def brife_of_body(self):
		return  re.sub('[!?*\[\]#(.*?\)|\[.*?\]=-_]',"",self.body[:200]) [:300]

	def post_preview(self):
		return self.body[:600]  # usefull when post is restricted

	# def delete_post(self):
		

	

	def save(self,  *args, **kwargs):
		self.brife = self.brife_of_body()
		self.slug = slugify(self.title[:50], allow_unicode=True)
		# locale.setlocale(locale.LC_ALL, "fa_IR")
		# jdatetime.set_locale('fa_IR')
		self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
		# self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
		super(Post, self).save( *args, **kwargs)

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ucomments')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pcomments')
	reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='rcomments', blank=True, null=True)
	is_reply = models.BooleanField(default=False)
	body = models.TextField(max_length=400)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.user} - {self.body[:30]}'



class Vote(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uvotes')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pvotes')

	def __str__(self):
		return f'{self.user} liked {self.post.slug}'



