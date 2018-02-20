from django.shortcuts import render,get_object_or_404,HttpResponse ,redirect


from .models import Post,Comment,PostReview,ForbiddenWords,ReplyComment ,Category ,Tag, PostTag ,User
from django.http import HttpResponseRedirect,request,HttpResponse ,JsonResponse
from .forms import CommentForm,ReplyForm ,createPost, categoryForm, tagForm, wordForm ,userForm ,edituserForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import Http404
from django.conf import settings
from django.contrib.auth.models import User



def adminhome(request):
    return render(request, "dashboard.html")

def allpost(request):
    posts =Post.objects.all()
    tags = PostTag.objects.all()
    context = {'posts': posts, 'tags': tags}
    return render(request, "posts.html", context)


def editpost(request, postId):
    post = get_object_or_404(Post, id=postId)
    tags = Tag.objects.all()
    checktag= PostTag.objects.filter(post=postId)
    form = createPost(instance=post)
    list=[]
    for check in checktag:
        list.append(check.tag.id)
    if request.method == "POST":
        some_var = request.POST.getlist('tag')
        form = createPost(request.POST ,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            oldposttag = PostTag.objects.filter(post=postId)
            oldposttag.delete()
            for ta in some_var:
                existTag = Tag.objects.get(id=ta)
                newposttag = PostTag.objects.create(post=post, tag=existTag)
                newposttag.save()
            return HttpResponseRedirect(reverse('posts'))
    return render(request, 'editpost.html', {'form': form, 'tags': tags, 'list': list})

def delete(request, postId):
    post = Post.objects.get(id=postId)
    post.delete()
    oldposttag = PostTag.objects.filter(post=postId)
    oldposttag.delete()
    return  HttpResponseRedirect(reverse('posts'))

def createpost(request):
    tags = Tag.objects.all()
    form =createPost()
    if request.method == "POST":
        some_var = request.POST.getlist('tag')
        form = createPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            lastpost= Post.objects.latest('id')
            for ta in some_var:
                existTag=Tag.objects.get(id=ta)
                newposttag = PostTag.objects.create(post=lastpost, tag=existTag)
                newposttag.save()
            return HttpResponseRedirect(reverse('posts'))
    return render(request, 'addpost.html', {'form': form, 'tags':tags})

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
            messages.success(request, "Successfully added Category", extra_tags='')
            return HttpResponseRedirect(reverse('cats'))
    return render(request, 'addcat.html', {'form': form})


def deletecat(request, catId):
    cat = Category.objects.get(id=catId)
    cat.delete()
    messages.success(request, "Successfully Deleted Category", extra_tags='')
    return  HttpResponseRedirect(reverse('cats'))

def editcat(request ,catId):
    cat = get_object_or_404(Category, id=catId)
    if request.method == "POST":
        form = categoryForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Edited Category", extra_tags='')
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
            messages.success(request, "Successfully added Tag", extra_tags='')
            return HttpResponseRedirect(reverse('tags'))
    return render(request, 'addtag.html', {'form': form})

def edittag(request, tagId):
    tag = get_object_or_404(Tag, id=tagId)
    if request.method == "POST":
        form = tagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Edited Tag", extra_tags='')
            return HttpResponseRedirect(reverse('tags'))
    else:
        form = tagForm(instance=tag)
    return render(request, 'addtag.html', {'form': form})

def deletetag(request, tagId):
    tag = Tag.objects.get(id=tagId)
    tag.delete()
    messages.success(request, "Successfully Deleted Tag", extra_tags='')
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
            messages.success(request, "Successfully Created new Forbidden Word", extra_tags='')
            return HttpResponseRedirect(reverse('words'))
    return render(request, 'addword.html', {'form': form})


def deleteword(request, wordId):
    word = ForbiddenWords.objects.get(id=wordId)
    word.delete()
    messages.success(request, "Successfully Deleted Forbidden Word", extra_tags='')
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
            user.set_password(request.POST['password'])
            user.save()
            messages.success(request, "Successfully added new user", extra_tags='')
            return HttpResponseRedirect(reverse('users'))
    return render(request, 'adduser.html', {'form': form})

def deleteuser(request ,userId):
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

def block(request):
    if request.is_ajax():
        userid = request.GET['id']
        user = get_object_or_404(User, id=userid)
        if user.is_active == 1:
            user.is_active = 0
            user.save()
            return JsonResponse({'is_active': user.is_active, "userid":user.id}, safe=False)
        else:
            user.is_active = 1
            user.save()
            return JsonResponse({'is_active': user.is_active, "userid":user.id}, safe=False)
    raise Http404

def promottoadmin(request):
    if request.is_ajax():
        userid = request.GET['id']
        user = get_object_or_404(User, id=userid)
        user.is_superuser = 1
        user.save()
        return JsonResponse({"userid":user.id}, safe=False)
    raise Http404


# Create your views here.
def home (request):
	#return HttpResponse("<h1>Home Page</h1>")
	all_Catagories=Category.objects.all()
	all_Posts=Post.objects.all()
	latest_Posts=Post.objects.all().order_by('-publish_date')[:3:1]
	latest_Post=Post.objects.all().order_by('-publish_date')[:1].get()
	context={"all_Catagories":all_Catagories ,
	"latest_Posts":latest_Posts,
	"all_Posts":all_Posts,
	"latest_Post":latest_Post}
	return render(request,"home.html",context)



def showCatPosts(request,cat_id):
	#return HttpResponse("<h1>showCatPosts</h1>")
	cat_name=Category.objects.get(id=cat_id).name
	all_Catagories=Category.objects.all()
	#cat_Posts=Post.objects.filter(cat_id=cat_id)
	latest_Posts=Post.objects.filter(cat_id=cat_id).order_by('-publish_date')
	latest_Post=Post.objects.filter(cat_id=cat_id).order_by('-publish_date')[:1].get()
	context={"all_Catagories":all_Catagories ,
	"latest_Posts":latest_Posts,
	"latest_Post":latest_Post,
	"cat_name":cat_name}
	return render(request,"CatPosts.html",context)	

def draw(len):
    i=1
    newword = "*"
    while(i<len):
        newword += "*"
        i += 1
    return newword
                
        
def getPost(request, post_id):

    #post
    po = Post.objects.get(id = post_id)

    #all Replies from db
    all_replies = ReplyComment.objects.all()

    #count likes and dislikes to exist user
    countLike = 0
    countDislike = 0

    countLike = PostReview.objects.filter(post_id = post_id,user_id =1,review =1).count() #count likes to exist user
    
    countDislike = PostReview.objects.filter(post_id = post_id,user_id =1,review =0).count() #count dislikes to exist user

    #all Likes and dislikes
    allLikes = PostReview.objects.filter(post_id = post_id,review =1).count()#alllikes to this post in server    
    DisLikes = PostReview.objects.filter(post_id = post_id,review =0).count()#alldisikes to this post in server
 
    #get bad words from db 
    all_words = ForbiddenWords.objects.all()

    #comments on post
    all_comments = Comment.objects.filter(post = post_id)
    form = CommentForm()
    formReply = ReplyForm()
   

    if request.method == "POST":
        
        form = CommentForm(request.POST)
        if form.is_valid():
            all_comments = form.save(commit=False)
            all_comments.user_id = 1
            all_comments.post_id = post_id
            myText = form.cleaned_data['commmentText']

            for word in all_words:
                myText=myText.replace(word.word, draw(word.wordLen))
            #messages.info(request, myText)
            all_comments.commmentText = myText
            form.save() #save post (comment,postID,userID)

            return HttpResponseRedirect('/social_Blog/post/'+post_id)
    
   
	
    context = {
        'AllLikes':allLikes,
        'AllDisLikes':DisLikes,
        'countLikes':countLike,
        'countDislikes':countDislike,
        "all_comments": all_comments,
        'form':form,
        'post':po,
        'formReply':formReply,
        'AllReplies':all_replies,
    }
    return render(request, 'post/post_details.html', context)
    
def reply(request,comment_id,post_id):
     #get bad words from db 
    all_words = ForbiddenWords.objects.all()

    #replies on comment
    all_replies = ReplyComment.objects.filter(comment = comment_id)
    formReply = ReplyForm()
    if request.method == "POST":
        
        formReply = ReplyForm(request.POST)
        if formReply.is_valid():
            all_replies = formReply.save(commit=False)
            all_replies.user_id = 1
            all_replies.comment_id = comment_id
            myText = formReply.cleaned_data['replyText']
            for word in all_words:
                myText=myText.replace(word.word, draw(word.wordLen))
            #messages.info(request, myText)
            all_replies.replyText = myText

           
            formReply.save() #save post (comment,postID,userID)
            return HttpResponseRedirect('/social_Blog/post/'+post_id)
 
    
def addLike(request,post_id):
   
    messages.info(request, post_id)
    postRev= PostReview.objects.filter(post_id = post_id,user_id =1,review =1).count()
    p = PostReview(post_id=post_id, user_id=1,review =1)
    
    if postRev == 0:
        ps = PostReview(post_id=post_id, user_id=1,review =1)
        ps.save()  
     
    else:
        pd = PostReview.objects.filter(post_id = post_id,user_id =1,review =1)
        pd.delete()  

   

    #count and discounts

    countLike = 0
    countDislike = 0

    countLike = PostReview.objects.filter(post_id = post_id,user_id =1,review =1).count()
    
    countDislike = PostReview.objects.filter(post_id = post_id,user_id =1,review =0).count()

    #all Likes and dislikes
    allLikes = PostReview.objects.filter(post_id = post_id,review =1).count()    
    DisLikes = PostReview.objects.filter(post_id = post_id,review =0).count()  

    data = {
            'AllLikes':allLikes,
        'AllDisLikes':DisLikes,
        'countLikes':countLike,
        'countDislikes':countDislike,
        }
  
    return JsonResponse(data,safe=False)
     
      


def DisLike(request, post_id):
    postRev= PostReview.objects.filter(post_id = post_id,user_id =1,review =0).count()
    
    if postRev == 0:
        ps = PostReview(post_id=post_id, user_id=1,review =0)
        ps.save()  
     
    else:
        pd = PostReview.objects.filter(post_id = post_id,user_id =1,review =0)
        pd.delete()  
      
    #count and discounts

    countLike = 0
    countDislike = 0

    countLike = PostReview.objects.filter(post_id = post_id,user_id =1,review =1).count()
    
    countDislike = PostReview.objects.filter(post_id = post_id,user_id =1,review =0).count()

    #all Likes and dislikes
    allLikes = PostReview.objects.filter(post_id = post_id,review =1).count()    
    DisLikes = PostReview.objects.filter(post_id = post_id,review =0).count()  

    data = {
            'AllLikes':allLikes,
        'AllDisLikes':DisLikes,
        'countLikes':countLike,
        'countDislikes':countDislike,
        }
  
    return JsonResponse(data,safe=False)   
    

