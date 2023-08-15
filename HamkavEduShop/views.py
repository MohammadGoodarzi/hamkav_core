from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from HamkavBlog.utils import UserPosts
from django.core.paginator import Paginator


class ProfileDashboardView(LoginRequiredMixin, View):
    
    template_name = "HamkavEduShop/profile/profile_dashboard.html"
    user_post = UserPosts()
    
    def get(self, request):
        posts = self.user_post.getPosts(request_user=request.user, post_status='all', result="count" )
        return render(request, context= {'posts_count': posts}, template_name= self.template_name )
    
    def post():
        pass
    
    
    
    
class ProfilePostsView(LoginRequiredMixin, View):
    
    template_name = "HamkavEduShop/profile/profile_posts.html"
    user_post = UserPosts()
    
    def get(self, request):
        posts = self.user_post.getPosts(request_user=request.user, post_status='all', result="list" )
        
        paginator = Paginator(posts, 16)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, context= {'posts': page_obj}, template_name= self.template_name )
    
    def post():
        pass