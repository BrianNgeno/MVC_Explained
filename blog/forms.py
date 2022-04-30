from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'content','slug', 'publisher','image')
        exclude = ['time_created']
        
        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the Blog title'
            }),
            "image": forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            "publisher": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the blog publisher name'
            }),
            'content': SummernoteWidget(attrs={
                'class':'form-control',
                'placeholder': 'Enter your blog content'
            }),         
            "slug": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'please enter your blog url'
            }),
            
        }


