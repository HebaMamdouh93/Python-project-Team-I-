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
        return str(self.user_id)

class Post(models.Model):
    text = models.CharField(max_length = 255)
    img = models.FileField()
    title = models.CharField(max_length = 255)
    publish_date=models.DateTimeField(auto_now_add=True,null=True)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)

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

class Comment(models.Model):
    commmentText = models.CharField(max_length = 255)
    user =  models.ForeignKey(User)
    post =  models.ForeignKey(Post)
    comTime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.commmentText

class ReplyComment(models.Model):
    replyText = models.CharField(max_length = 255)
    user =  models.ForeignKey(User)
    comment =  models.ForeignKey(Comment)
    repTime = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.replyText

class PostReview(models.Model):
    post =  models.ForeignKey(Post)
    user =  models.ForeignKey(User)
    review = models.IntegerField()

    def __str__(self):
        return self.review
