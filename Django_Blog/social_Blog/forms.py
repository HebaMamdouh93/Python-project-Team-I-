from django import forms
from . import models
from .models import Comment,ReplyComment

class createPost(forms.ModelForm):
    class Meta:
         model = models.Post
         fields = ("title", "text",  "cat", "img",)
         widgets = {
             'title': forms.TextInput(attrs={'class': 'form-control border-input '}),
             'text': forms.Textarea(attrs={'class': 'form-control border-input'}),
             "cat": forms.Select(attrs={'class': 'form-control border-input '})
         }

class categoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ("name",)

class tagForm(forms.ModelForm):
    class Meta:
        model = models.Tag
        fields = ("tagName",)

class wordForm(forms.ModelForm):
    class Meta:
        model =models.ForbiddenWords
        fields = ("word",)

class userForm(forms.ModelForm):
    class Meta:
        model =models.User
        fields = ("username", "email" ,"first_name", "last_name", "password")
        widgets = {
            'username':forms.TextInput(attrs={'class': 'form-control border-input'}),
            'email':forms.TextInput(attrs={'class': 'form-control border-input '}),
            'first_name':forms.TextInput(attrs={'class': 'form-control border-input'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control border-input'}),
            'password':forms.TextInput(attrs={'class': 'form-control border-input', 'type': 'password'}),
        }

class edituserForm(forms.ModelForm):
    class Meta:
        model =models.User
        fields = ("username", "email", "first_name", "last_name")
        widgets = {
            'username':forms.TextInput(attrs={'class': 'form-control border-input '}),
            'email':forms.TextInput(attrs={'class': 'form-control border-input'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control border-input'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control border-input'}),
        }




class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('commmentText',)
        widgets = {
        'commmentText': forms.Textarea(attrs={'cols': 40, 'rows': 3 , }),
        
        }

class ReplyForm(forms.ModelForm):
    
    class Meta:
        model = ReplyComment
        fields = ('replyText',)
        widgets = {
        'replyText': forms.Textarea(attrs={'cols': 20, 'rows': 3}),
        
        }
        

