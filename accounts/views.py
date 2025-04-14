from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            # login automático após o cadastro
            login(request, user)
            return redirect('feed')  # depois vamos criar essa URL
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

@login_required
def user_list_view(request):
    users = User.objects.exclude(id=request.user.id).filter(is_superuser=False)
    return render(request, 'accounts/user_list.html', {'users': users})

@login_required
def follow_view(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    request.user.profile.following.add(target_user.profile)
    return redirect('user_list')

@login_required
def unfollow_view(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    request.user.profile.following.remove(target_user.profile)
    return redirect('user_list')

@login_required
def profile_view(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    posts = target_user.post_set.all().order_by('-created_at')
    return render(request, 'accounts/profile.html', {
        'target_user': target_user,
        'posts': posts
    })