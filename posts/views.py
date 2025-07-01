from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__name', 'title']

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]      
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class PostRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  
    
    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)