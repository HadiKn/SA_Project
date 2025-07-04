from django.urls import path
from .views import CommentListView, CommentCreateView, CommentRetrieveView, PostCommentListView

urlpatterns = [
    # list all comments
    path('list/', CommentListView.as_view(), name='comment-list'),
    # create a comment
    path('create/', CommentCreateView.as_view(), name='comment-create'),
    # list comments for a specific post
    path('post/<int:post_id>/', PostCommentListView.as_view(), name='post-comment-list'),
    # modify or delete a comment
    path('retrieve/<int:pk>/', CommentRetrieveView.as_view(), name='comment-detail'),
]       
