from .models import Post, Comment, Vote, Category2

class UserPosts:
    def __init__(self) -> None:
        pass
        # self.user = user
    def getPosts(self, request_user, post_status, result, search = None):
        if post_status == 'all':
            if result == "count":
                res = Post.objects.filter(user = request_user).count()
                return res
            if result == "list":
                res = Post.objects.filter(user = request_user).order_by('is_published', '-is_deleted', '-created')
                return res
        