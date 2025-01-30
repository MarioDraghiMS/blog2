from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'image']
        # widgets = {
        #     'content': forms.Textarea(attrs={'rows': 10}),
        # }