from django.http import request
from django.shortcuts import HttpResponse ,redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from .forms import createPost, categoryForm, tagForm, wordForm ,userForm ,edituserForm
from .models import Post, Category, Tag, PostTag, ForbiddenWords,User
from django.conf import settings
import random

def allpost(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    context = {'posts': posts , 'tags' :tags }
    return render(request, "posts.html", context)


def editpost(request, postId):
    post = get_object_or_404(Post, id=postId)
    if request.method == "POST":
        form = createPost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('posts'))
    else:
        form = createPost(instance=post)
    return render(request, 'add.html', {'form': form})

def delete(request, postId):
    post = Post.objects.get(id=postId)
    post.delete()
    return  HttpResponseRedirect(reverse('posts'))


def createpost(request):
    #tags = Tag.objects.all()
    form =createPost()
    if request.method == "POST":
        form = createPost(request.POST, request.FILES)
        #some_var = request.POST.getlist('tag')
        if form.is_valid():
            form.save()
        #     lastPost= Post.objects.latest('id')
        #     for ta in some_var:
        #         existTag=Tag.objects.get(id=ta)
        #         newposttag = PostTag.objects.create(post=lastPost, tag=existTag)
        #         newposttag.save()
            return HttpResponseRedirect(reverse('posts'))
    return render(request, 'add.html', {'form': form})


def allcats(request):
    cats = Category.objects.all()
    context = {"cats": cats}
    return render(request, 'categorys.html', context)

def createcat(request):
    form =categoryForm()
    if request.method == "POST":
        form = categoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.save()
            return HttpResponseRedirect(reverse('cats'))
    return render(request, 'addcat.html', {'form': form})


def deletecat(request, catId):
    cat = Category.objects.get(id=catId)
    cat.delete()
    return  HttpResponseRedirect(reverse('cats'))

def editcat(request ,catId):
    cat = get_object_or_404(Category, id=catId)
    if request.method == "POST":
        form = categoryForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cats'))
    else:
        form = categoryForm(instance=cat)
    return render(request, 'addcat.html', {'form': form})


def alltags(request):
    tags = Tag.objects.all()
    cont ={"tags" : tags}
    return render(request, 'tags.html', cont)


def createtag(request):
    form = tagForm()
    if request.method == "POST":
        form = tagForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tags'))
    return render(request, 'addtag.html', {'form': form})

def edittag(request, tagId):
    tag = get_object_or_404(Tag, id=tagId)
    if request.method == "POST":
        form = tagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tags'))
    else:
        form = tagForm(instance=tag)
    return render(request, 'addtag.html', {'form': form})

def deletetag(request, tagId):
    tag = Tag.objects.get(id=tagId)
    tag.delete()
    return HttpResponseRedirect(reverse('tags'))


def createtagAjax(request):
    tag = request.GET.get('tag', None)
    return HttpResponse(tag)

def allwords(request):
    words = ForbiddenWords.objects.all()
    cont = {"words": words}
    return render(request, 'word.html', cont)

def createword(request):
    form = wordForm()
    if request.method == "POST":
        form = wordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            word.wordLen =len(word.word)
            word.save()
            return HttpResponseRedirect(reverse('words'))
    return render(request, 'addword.html', {'form': form})


def deleteword(request, wordId):
    word = ForbiddenWords.objects.get(id=wordId)
    word.delete()
    return HttpResponseRedirect(reverse('words'))

def editword(request, wordId):
    word = get_object_or_404(ForbiddenWords, id=wordId)
    if request.method == "POST":
        form = wordForm(request.POST, instance=word)
        if form.is_valid():
            word = form.save(commit=False)
            word.wordLen = len(word.word)
            word.save()
            return HttpResponseRedirect(reverse('words'))
    else:
        form = wordForm(instance=word)
    return render(request, 'addword.html', {'form': form})


def allusers(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def createuser(request):
    form = userForm()
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = 0
            user.is_active = 1
            user.save()
            return HttpResponseRedirect(reverse('users'))
    return render(request, 'adduser.html', {'form': form})

def deleteword(request ,userId):
    user = User.objects.get(id=userId)
    user.delete()
    return HttpResponseRedirect(reverse('users'))

def edituser(request ,userId):
    user = get_object_or_404(User, id=userId)
    if request.method == "POST":
        form = edituserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users'))
    else:
        form = edituserForm(instance=user)
    return render(request, 'edituser.html', {'form': form})
