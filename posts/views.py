from rest_framework import generics,filters
from .models import Post
from .serializers import PostSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__name','title']

class PostCreateView(generics.CreateAPIView):
    pass

class PostRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    pass