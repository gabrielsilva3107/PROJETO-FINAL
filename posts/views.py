from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from accounts.models import Profile
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def feed_view(request):
    profile = request.user.profile
    following_users = [p.user for p in profile.following.all()]

    # Criação do post via POST
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Post.objects.create(user=request.user, content=content)
            return redirect('feed')

    # Mostrar feed
    posts = Post.objects.filter(user__in=following_users + [request.user])
    posts = posts.order_by('-created_at')

    return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('feed'))

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user == request.user:
        post.delete()
    return redirect('feed')

from .models import Post, Comment

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        content = request.POST.get("comment")
        if content:
            Comment.objects.create(post=post, user=request.user, content=content)
    return redirect('feed')

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user == request.user:
        comment.delete()
    return redirect('feed')
