from django.urls import path,include
from .views import PostListView,PostCreateView


urlpatterns = [
    path('list/', PostListView.as_view()),
    path('create/', PostCreateView.as_view()),

    ]
         