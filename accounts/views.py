from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm


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

@login_required
def edit_profile(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('feed')

    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
