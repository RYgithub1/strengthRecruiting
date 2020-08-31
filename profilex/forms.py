from django import forms
from .models import Post, Scout


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # author -> loginUser
        fields = ('title', 'text', 'thumbnail', 'upload',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'thumbnail': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
            'upload': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
        }


class ScoutForm(forms.ModelForm):
    class Meta:
        model = Scout
        fields = ('author', 'text',)
