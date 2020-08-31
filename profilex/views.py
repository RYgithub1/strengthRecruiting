# サインアップ
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# ログイン
from django.contrib.auth.decorators import login_required

# プロフィール/スカウト
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm, ScoutForm, SignupForm


# サインアップ
class SignUp(CreateView):
    form_class = SignupForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())


# プロフィール一覧
def post_list(request):
    posts = Post.objects.filter(
        created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'profilex/post_list.html', {'posts': posts})


# プロフィール詳細
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'profilex/post_detail.html', {'post': post})


# プロフィール新規
# (post_edit_htm)save -> request.POST にデータ格納
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'profilex/post_edit.html', {'form': form})


# プロフィール編集
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # フォーム作成時、そのポストをinstanceとして渡す
    if request.method == "POST":
        # 編集フォームを保存
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        # 編集フォームを表示
        form = PostForm(instance=post)
    return render(request, 'profilex/post_edit.html', {'form': form})


# プロフィール削除
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


# スカウト新規
def add_scout_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ScoutForm(request.POST)
        if form.is_valid():
            scout = form.save(commit=False)
            scout.post = post
            scout.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ScoutForm()
    return render(request, 'profilex/add_scout_to_post.html', {'form': form})
