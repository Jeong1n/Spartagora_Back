from django.db import models
from django.forms import CharField
from user.models import User
from taggit.managers import TaggableManager
# Create your models here.

# like 모델,tag 앱 논의 필요



class UpperCategory(models.Model):    
    upper_category = models.CharField(max_length=100)

    def __str__(self):
        return self.upper_category


class LowerCategory(models.Model):
    upper_category = models.ForeignKey(UpperCategory, on_delete=models.CASCADE)
    lower_category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.lower_category


class Article(models.Model):
    user = models.ForeignKey(User, related_name="article_user",on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    image = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    lower_category = models.ForeignKey(LowerCategory, on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)
    count = models.IntegerField(default = 0)
    # like = models.ManyToManyField(User, related_name="article_like")
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    article = models. ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)