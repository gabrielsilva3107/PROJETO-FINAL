from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from accounts.models import Profile

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
