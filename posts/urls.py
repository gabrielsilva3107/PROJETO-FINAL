from django.urls import path
from .views import add_comment, delete_comment, delete_post, feed_view, toggle_like

urlpatterns = [
    path('', feed_view, name='feed'),
    path('like/<int:post_id>/', toggle_like, name='toggle_like'),
    path('post/delete/<int:post_id>/', delete_post, name='delete_post'),
    path('comment/<int:post_id>/', add_comment, name='add_comment'),
    path('comment/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
]
