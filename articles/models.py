from django.db import models
from user.models import User


class Article(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True,blank=True, max_length=3000)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Article'