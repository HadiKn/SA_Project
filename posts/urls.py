from django.urls import path,include
from .views import PostListView,PostCreateView,PostRetrieveView


urlpatterns = [
    # list all posts
    path('list/', PostListView.as_view()),
    # create a post
    path('create/', PostCreateView.as_view()),
    # get or modify or delete a post
    path('retrieve/<int:pk>/', PostRetrieveView.as_view()),

    ]
         