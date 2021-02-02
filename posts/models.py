from django.db import models
from accounts.models import UserAccounts
from django.contrib.auth import get_user_model




class POST(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    caption=models.TextField()
    image=models.ImageField(upload_to='post')
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
class LIKE(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='user_like')
    post=models.ForeignKey(POST,on_delete=models.CASCADE,related_name='post_like')
    class Meta:
        unique_together=['user','post']
class COMMENT(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='user_comments')
    post=models.ForeignKey(POST,on_delete=models.CASCADE,related_name='post_comments')
class HASHTAG(models.Model):
    tag=models.TextField(max_length=40)
    post=models.ManyToManyField(POST)


# Create your models here.
