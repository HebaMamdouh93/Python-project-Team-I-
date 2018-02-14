from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name


class UserCat(models.Model):
    user = models.ForeignKey(User)
    cat = models.ForeignKey(Category)    

    def __str__(self):
        return self.user_id

class Post(models.Model):
    text = models.CharField(max_length = 255)
    img = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    likes = models.IntegerField(null=True)
    unLikes = models.IntegerField(null=True)
    publish_date=models.DateTimeField(auto_now_add=True,null=True)
    user =  models.ForeignKey(User)
    cat = models.ForeignKey(Category)

    def __str__(self):
        return self.title

class Tag(models.Model):
    tagName = models.CharField(max_length = 255)

    def __str__(self):
        return self.tagName

class PostTag(models.Model):
    post = models.ForeignKey(Post)
    tag = models.ForeignKey(Tag)    

    def __str__(self):
        return self.post

class ForbiddenWords(models.Model):
    word = models.CharField(max_length = 255)
    wordLen = models.IntegerField()    

    def __str__(self):
        return self.word
