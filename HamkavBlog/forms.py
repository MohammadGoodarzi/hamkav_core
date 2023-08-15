from django import forms
from .models import Post, Comment, Category2
from treebeard.forms import movenodeform_factory, MoveNodeForm

# from markdownx.fields import MarkdownxFormField

class CategoryForm(MoveNodeForm):
    class Meta:
        model = Category2
        exclude = ('sib_order', 'parent')
        
class PostCreateUpdateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('body','title', 'category2', 'is_published' )
		labels = {
            'category2': 'دسته بندی',
            'is_published': ' پست منتشر شود؟',
        }
		widgets = {
			'body': forms.Textarea(attrs={'id':'markdown_input' , 'class':'form-control shadow-lg'}),
			'category2': forms.Select(attrs={'class':'form-control shadow-lg'}),
			'title': forms.TextInput(attrs={'class':'form-control shadow-lg'}),
			# 'is_published': forms.BooleanField(),
			# 'title': forms.TextInput(attrs={'class':'form-control shadow-lg'}),
		}


class CommentCreateForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)
		widgets = {
			'body': forms.Textarea(attrs={'class':'form-control'})
		}


class CommentReplyForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)


class PostSearchForm(forms.Form):
	search = forms.CharField()