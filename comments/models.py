from django.db import models
from django.contrib.auth.models import User 
from posts.models import  Post

class Comment(models.Model) :
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    post = models.ForeignKey(Post,on_delete= models.CASCADE,related_name='comments')
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content 