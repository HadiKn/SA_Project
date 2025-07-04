from django.urls import path
from .views import CommentListView, CommentCreateView, CommentRetrieveView, PostCommentListView

urlpatterns = [
    path('list/', CommentListView.as_view(), name='comment-list'),
    path('create/', CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:post_id>/', PostCommentListView.as_view(), name='post-comment-list'),
    path('retrieve/<int:pk>/', CommentRetrieveView.as_view(), name='comment-detail'),
]       
