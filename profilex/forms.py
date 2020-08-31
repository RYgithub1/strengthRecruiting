# サインアップ
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# プロフィール/スカウト
from django import forms
from .models import Post, Scout


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


# models.pyでFieldを定義 -> ModelForm(forms.py)でフォームを作成
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
