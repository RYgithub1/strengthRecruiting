from django.shortcuts import render
from django.utils import timezone
# 別のファイル(.models)に用意したコード(Post)をインクルード
from .models import Post


def post_list(request):
    posts = Post.objects.filter(
        created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'profilex/post_list.html', {'posts': posts})
