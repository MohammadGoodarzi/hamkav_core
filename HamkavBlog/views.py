from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
# from django.views.generic import ListView
from .models import Post, Comment, Vote, Category2
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import PostCreateUpdateForm, CommentCreateForm, CommentReplyForm, PostSearchForm, CategoryForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from markdownx.utils import markdownify
from django.core.paginator import Paginator


# class HomeView(View):
# 	form_class = PostSearchForm

# 	def get(self, request):
# 		posts = Post.objects.all()
# 		if request.GET.get('search'):
# 			posts = posts.filter(body2__contains=request.GET['search'])
# 		return render(request, 'HamkavBlog/index.html', {'posts':posts, 'form':self.form_class})


class HomeListView(View):
	form_class = PostSearchForm
    
    
	def get(self, request):
		posts = Post.objects.filter(is_deleted = None, is_published = True )
		if request.GET.get('search'):
			posts = posts.filter(body__contains=request.GET.get('search'))
		paginator = Paginator(posts, 16)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		return render(request, 'HamkavBlog/index.html', {'posts':page_obj, 'form':self.form_class})


class AllUserPostView(View):
	form_class = PostSearchForm
    
	def get(self, request):
		posts = Post.objects.filter(user = request.user)
		if request.GET.get('search'):
			posts = posts.filter(body__contains=request.GET.get('search'))
		paginator = Paginator(posts, 16)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		return render(request, 'HamkavBlog/index.html', {'posts':page_obj, 'form':self.form_class})



class PostDetailView(View):
	form_class = CommentCreateForm
	form_class_reply = CommentReplyForm

	def setup(self, request, *args, **kwargs):
		self.post_instance = get_object_or_404(Post, pk=kwargs['post_id'], slug=kwargs['post_slug'], is_deleted = None)
  
		return super().setup(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		comments = self.post_instance.pcomments.filter(is_reply=False)
		can_like = False
		if request.user.is_authenticated and self.post_instance.user_can_like(request.user):
			can_like = True
   
		
			
      
   
		if not request.user.is_authenticated:
			self.post_instance.body = self.post_instance.post_preview()+'.....(جهت مشاهده ادامه این مقاله لطفا وارد شوید)'
		if request.user.is_authenticated and self.post_instance.is_restricted:
			self.post_instance.body = self.post_instance.post_preview()+'.....(جهت مشاهده ادامه این مقاله لطفا عضو ویژه منتولینک شوید)'
      
			
   
   
		# self.post_instance.body2 = markdownify(self.post_instance.body2)
		# print(self.post_instance.body)
		return render(request, 'HamkavBlog/detail.html', {'post':self.post_instance, 'comments':comments, 'form':self.form_class, 'reply_form':self.form_class_reply, 'can_like':can_like})

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			new_comment = form.save(commit=False)
			new_comment.user = request.user
			new_comment.post = self.post_instance
			new_comment.save()
			messages.success(request, ' پاسخ شما ثبت شد. ', 'success')
			return redirect('HamkavBlog:post_detail', self.post_instance.id, self.post_instance.slug)


class PostDeleteView(LoginRequiredMixin, View):
	def get(self, request, post_id):
		post = get_object_or_404(Post, pk=post_id)
		if post.user.id == request.user.id:
			# post.delete()   # حذف فیزیکی
			post.is_deleted = True
			post.save() #حذف منطقی 
			messages.success(request, ' پست مورد نظر شما حذف شد ',  'success')
		else:
			messages.error(request, 'شما نمی توانید این پست را حذف کنید', 'danger')
		return redirect('HamkavBlog:home')


class PostUpdateView(LoginRequiredMixin, View):
	form_class = PostCreateUpdateForm
	template_name = 'HamkavBlog/update.html'
 

	def setup(self, request, *args, **kwargs):
		self.post_instance = get_object_or_404(Post, pk=kwargs['post_id']) 
   
		return super().setup(request, *args, **kwargs)

	def dispatch(self, request, *args, **kwargs):
		post = self.post_instance
		if not post.user.id == request.user.id:
			messages.error(request, 'شما نمی توانید این پست را ویرایش کنید', 'danger')
			return redirect('HamkavBlog:home')
		return super().dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		post = self.post_instance
  
		form = self.form_class(instance=post)
		# print(form.is_published)
		return render(request, self.template_name, {'form':form, 'is_published':post.is_published})

	def post(self, request, *args, **kwargs):
		post = self.post_instance
		form = self.form_class(request.POST, instance=post)
		if form.is_valid():
			new_post = form.save(commit=False)
			# new_post.slug = slugify(form.cleaned_data['body'][:30])
			new_post.save()
			messages.success(request, 'پست شما با موفقیت به روز شد', 'success')
			return redirect('HamkavBlog:post_detail', post.id, post.slug)
		messages.warning(request,'اشکالی در اطلاعات ارسالی وجود دارد لطفا ورودی ها کنترل نمایید.' )
		return render(request, self.template_name, {"form":form})


class PostCreateView(LoginRequiredMixin, View):
	form_class = PostCreateUpdateForm
	template_name = 'HamkavBlog/create.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class
		# tree = Category2.dump_bulk()
		# tree = Category2.get_annotated_list()
		tree = Category2.get_tree(parent=None)
		# branch = Category2.dump_bulk(node_obj)
		return render(request, self.template_name, {'form':form, 'category2':tree})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			# new_post.slug = slugify(form.cleaned_data['body2'][:30])
			new_post.user = request.user
			new_post.save()
			messages.success(request, 'پست شما به زودی منتشر میشود', 'success')
			return redirect('HamkavBlog:post_detail', new_post.id, new_post.slug)
		# print(form)
		messages.warning(request,'اشکالی در اطلاعات ارسالی وجود دارد لطفا ورودی ها کنترل نمایید.' )
		return render(request, self.template_name, {"form":form})

class PostAddReplyView(LoginRequiredMixin, View):
	form_class = CommentReplyForm

	def post(self, request, post_id, comment_id):
		post = get_object_or_404(Post, id=post_id)
		comment = get_object_or_404(Comment, id=comment_id)
		form = self.form_class(request.POST)
		if form.is_valid():
			reply = form.save(commit=False)
			reply.user = request.user
			reply.post = post
			reply.reply = comment
			reply.is_reply = True
			reply.save()
			messages.success(request, 'پاسخ شما ثبت شد.', 'success')
		return redirect('HamkavBlog:post_detail', post.id, post.slug)


class PostLikeView(LoginRequiredMixin, View):
	def get(self, request, post_id):
		post = get_object_or_404(Post, id=post_id)
		like = Vote.objects.filter(post=post, user=request.user)
		if like.exists():
			messages.error(request, 'این پست را لایک کردید!', 'danger')
		else:
			Vote.objects.create(post=post, user=request.user)
			messages.success(request, '\u2764 این پست رو دوست داشتید', 'success')
		return redirect('HamkavBlog:post_detail', post.id, post.slug)