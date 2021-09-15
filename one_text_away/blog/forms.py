from django import forms
from blog.models import Comment,Posts
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','body']


class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=['title','slug','intro','body']