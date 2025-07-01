from django.urls import path,include
from .views import PostListView,PostCreateView,PostRetrieveView


urlpatterns = [
    path('list/', PostListView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('retrieve/<int:pk>/', PostRetrieveView.as_view()),

    ]
         