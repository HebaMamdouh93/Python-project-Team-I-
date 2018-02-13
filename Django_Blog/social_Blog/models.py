from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    userType = models.IntegerField()
    blockType = models.IntegerField()

    def __str__(self):
        return self.userName

class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class UserCat(models.Model):
    user = models.ForeignKey(User)
    cat = models.ForeignKey(Category)    

class Post(models.Model):
    text = models.CharField(max_length = 255)
    img = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    likes = models.IntegerField(null=True)
    unLikes = models.IntegerField(null=True)
    user =  models.ForeignKey(User)
    cat = models.ForeignKey(Category)

    def __str__(self):
        return self.title

class Tag(models.Model):
    tagName = models.CharField(max_length = 255)

    def __str__(self):
        return self.tagName
