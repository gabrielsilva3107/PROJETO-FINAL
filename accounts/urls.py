from django.urls import path
from .views import (
    follow_view,
    profile_view,
    register_view,
    CustomLoginView,
    unfollow_view,
    user_list_view,
    edit_profile
)
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('users/', user_list_view, name='user_list'),
    path('follow/<int:user_id>/', follow_view, name='follow'),
    path('unfollow/<int:user_id>/', unfollow_view, name='unfollow'),
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('edit/', edit_profile, name='edit_profile'),

    # Troca de senha
    path('trocar-senha/', PasswordChangeView.as_view(
        template_name='accounts/change_password.html',
        success_url='/accounts/senha-ok/'
    ), name='change_password'),
    path('senha-ok/', PasswordChangeDoneView.as_view(
        template_name='accounts/change_password_done.html'
    ), name='password_change_done'),
]
