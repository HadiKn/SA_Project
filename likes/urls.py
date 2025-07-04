from django.urls import path
from .views import (
    LikeListView,
    PostLikeListView,
    LikeCreateView,
    LikeDeleteView,
    UserLikesView
)

urlpatterns = [
    # List all likes
    path('list/', LikeListView.as_view(), name='like-list'),
    
    # List likes for a specific post
    path('post/<int:post_id>/', PostLikeListView.as_view(), name='post-like-list'),
    
    # Create a new like
    path('create/', LikeCreateView.as_view(), name='like-create'),
    
    # Unlike a post (delete like)
    path('delete/<int:pk>/', LikeDeleteView.as_view(), name='like-delete'),
    
    # List all posts liked by the current user
    path('user/me/', UserLikesView.as_view(), name='user-likes'),
]
