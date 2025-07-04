from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include('posts.urls')),
    path('api/comments/', include('comments.urls')),  
    path('api/likes/', include('likes.urls')),  
    path('api/users/', include('users.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
