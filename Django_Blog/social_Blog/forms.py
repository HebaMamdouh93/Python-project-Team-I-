from django import forms
from . import models
from .models import Comment,ReplyComment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login , get_user_model
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
        'commmentText': forms.Textarea(attrs={'cols': 40, 'rows': 3}),

        }

class ReplyForm(forms.ModelForm):

    class Meta:
        model = ReplyComment
        fields = ('replyText',)
        widgets = {
        'replyText': forms.Textarea(attrs={'cols': 10, 'rows': 3}),

        }



class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args , **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate (username=username , password=password)
            if not user:
                raise forms.ValidationError("not an existing user")
            if not user.check_password(password):
                raise forms.ValidationError("incorrect password")
        return super(UserLoginForm,self).clean(*args,**kwargs)






class UserRegisterForm (forms.ModelForm):
    email= forms.EmailField(label='Email address')
    email2= forms.EmailField(label='confirm Email')
    password=forms.CharField(widget=forms.PasswordInput)
    username=forms.CharField(label='user name')

    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'email2' ,
                  'password']

        widgets = {
             'username': forms.TextInput(attrs={'class': 'form-control '}),
             'email': forms.Textarea(attrs={'class': 'form-control '}),
             'email2': forms.TextInput(attrs={"type": 'file'}),
             "password  ": forms.Select(attrs={'class': 'form-control '}),
         }


    def clean(self,*args,**kwargs):
        print(self.cleaned_data)
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        print(email,email2)
        if email != email2:
            raise forms.ValidationError("not matched email")

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("this email is already registered")

    #    username_qs = User.objects.filter(username=username)
    #    if username_qs.exists():
    #        raise forms.ValidationError("this user name is already registered")


        return super (UserRegisterForm,self).clean(*args , **kwargs)

    def clean_email2 (self):
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        print(email,email2)
        if email != email2:
            raise forms.ValidationError("not matched email")

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("this email is already registered")
        return email
