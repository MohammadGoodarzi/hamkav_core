from django.urls import path, re_path
from . import views


app_name = 'HamkavBlog'
urlpatterns = [
	path('', views.HomeListView.as_view(), name='home'),
	# path('', views.HomeView.as_view(), name='home'),
	path('post/<int:post_id>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
	# path('post/<int:post_id>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
	re_path(r'post/(?P<post_id>[0-9]+)/(?P<post_slug>[-\w]+)/', views.PostDetailView.as_view(), name='post_detail'),
	path('post/delete/<int:post_id>/', views.PostDeleteView.as_view(), name='post_delete'),
	path('post/update/<int:post_id>/', views.PostUpdateView.as_view(), name='post_update'),
	path('post/create/', views.PostCreateView.as_view(), name='post_create'),
	path('reply/<int:post_id>/<int:comment_id>/', views.PostAddReplyView.as_view(), name='add_reply'),
	path('like/<int:post_id>/', views.PostLikeView.as_view(), name='post_like'),
]