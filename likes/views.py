from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .models import Like
from .serializers import LikeSerializer
from posts.models import Post

# Create your views here.

class LikeListView(generics.ListAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        return Like.objects.all().order_by('-created_at')

class PostLikeListView(generics.ListAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Like.objects.filter(post_id=post_id).order_by('-created_at')

class LikeCreateView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        post = get_object_or_404(Post, id=post_id)
        
        # Check if user already liked the post
        if Like.objects.filter(user=self.request.user, post=post).exists():
            raise PermissionDenied("You have already liked this post.")
            
        serializer.save(user=self.request.user, post=post)

class LikeDeleteView(generics.DestroyAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)
    
    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserLikesView(generics.ListAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Like.objects.filter(user=self.request.user).order_by('-created_at')
