from django import forms
from .models import Post, Comment, Story


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['story']
