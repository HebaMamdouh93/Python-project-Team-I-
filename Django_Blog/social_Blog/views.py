from django.shortcuts import render,get_object_or_404,HttpResponse ,redirect
from .models import Post,Comment,PostReview,ForbiddenWords,ReplyComment ,Category ,Tag, PostTag ,User
from django.http import HttpResponseRedirect,request,HttpResponse ,JsonResponse
from .forms import CommentForm,ReplyForm ,createPost, categoryForm, tagForm, wordForm ,userForm ,edituserForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth import(authenticate,get_user_model,login,logout,)
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserLoginForm , UserRegisterForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


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
    form =createPost()
    if request.method == "POST":
        form = createPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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
    
    likedisable=""
    dislikedisable=""
    
    #get all categories
    all_Catagories = Category.objects.all()
 
    userId = 0
    #get loogeduser Id
    if request.user.is_authenticated():
        username = request.user.username
        userId = User.objects.get(username=username).pk
     
   

    #comments on post
    all_comments = Comment.objects.filter(post = post_id)

    #post
    po = Post.objects.get(id = post_id)

    #all tags to this post
    tags = PostTag.objects.filter(post_id = post_id)

    #all Replies from db
    all_replies = ReplyComment.objects.all()
    all_words = ForbiddenWords.objects.all()
    for reply in all_replies:
        for word in all_words:
            reply.replyText=reply.replyText.replace(word.word, draw(word.wordLen))

    #count likes and dislikes to exist user
    countLike = 0
    countDislike = 0

    countLike = PostReview.objects.filter(post_id = post_id,user_id =userId,review =1).count() #count likes to exist user

    if(countLike == 1):
        likedisable = "invisible"

    countDislike = PostReview.objects.filter(post_id = post_id,user_id =userId,review =0).count() #count dislikes to exist user

    if(countDislike == 1):
        dislikedisable = "invisible"


    #all Likes and dislikes
    allLikes = PostReview.objects.filter(post_id = post_id,review =1).count()#alllikes to this post in server
    DisLikes = PostReview.objects.filter(post_id = post_id,review =0).count()#alldisikes to this post in server

    #get bad words from db
    all_words = ForbiddenWords.objects.all()
    for comment in all_comments:
        for word in all_words:
            comment.commmentText=comment.commmentText.replace(word.word, draw(word.wordLen))
            

    #comments on post
    #all_comments = Comment.objects.filter(post = post_id)
    form = CommentForm()
    formReply = ReplyForm()


    if request.method == "POST":

        form = CommentForm(request.POST)
        if form.is_valid():
            all_comments = form.save(commit=False)
            all_comments.user_id = userId
            all_comments.post_id = post_id
           
            form.save() #save post (comment,postID,userID)
            commentobj= Comment.objects.filter().order_by('-id')[0]
            for word in all_words:
                commentobj.commmentText=commentobj.commmentText.replace(word.word, draw(word.wordLen))
                formatedDateCom = commentobj.comTime.strftime("%b.%d, %Y, %I:%M%p")
            data = {
                  'commentUser':commentobj.user.username,
                  'commentText':commentobj.commmentText,
                  'commentTime':formatedDateCom,
                  'commentId':commentobj.id,
                  'postId': post_id,
                   }
       
            return JsonResponse(data,safe=False)
            #return HttpResponseRedirect('/social_Blog/post/'+post_id)



    context = {
        'all_Catagories':all_Catagories,
        'AllLikes':allLikes,
        'AllDisLikes':DisLikes,
        'countLikes':countLike,
        'countDislikes':countDislike,
        "all_comments": all_comments,
        'form':form,
        'post':po,
        'formReply':formReply,
        'AllReplies':all_replies,
        'AllTags':tags,
        'disableLike':likedisable,
        'disableDislike':dislikedisable,
    }
    return render(request, 'post/post_details.html', context)

@csrf_exempt
def reply(request,comment_id,post_id):
    #get bad words
    all_words = ForbiddenWords.objects.all()

    #text
    replyText = request.POST.get('reply',"none")
    
    #get loogeduser Id
    username = request.user.username
    userId = User.objects.get(username=username).pk
    
    #replies on comment
    all_replies = ReplyComment()
    all_replies.user_id = userId
    all_replies.comment_id = comment_id
    all_replies.replyText = replyText
    all_replies.save() #save post (comment,postID,userID)
            

    Replyobj= ReplyComment.objects.filter().order_by('-id')[0]
       
    for word in all_words:
                Replyobj.replyText=Replyobj.replyText.replace(word.word, draw(word.wordLen))
                formatedDate = Replyobj.repTime.strftime("%b.%d, %Y, %I:%M%p")
    
    data = {
                  'replyUser':Replyobj.user.username,
                  'replyText':Replyobj.replyText,
                  'replyComment':Replyobj.comment_id,
                  'replyTime':formatedDate,
                   }

    return JsonResponse(data,safe=False)
   


def addLike(request,post_id):

    #get loogeduser Id
    if request.user.is_authenticated():
        username = request.user.username
        userId = User.objects.get(username=username).pk

    #messages.info(request, post_id)
    postRev= PostReview.objects.filter(post_id = post_id,user_id =userId,review =1).count()
    p = PostReview(post_id=post_id, user_id=userId,review =1)

    if postRev == 0:
        ps = PostReview(post_id=post_id, user_id=userId,review =1)
        ps.save()

    else:
        pd = PostReview.objects.filter(post_id = post_id,user_id =userId,review =1)
        pd.delete()



    #count and discounts
    
    countLike = 0
    countDislike = 0

    countLike = PostReview.objects.filter(post_id = post_id,user_id =userId,review =1).count()

    countDislike = PostReview.objects.filter(post_id = post_id,user_id =userId,review =0).count()

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

    #get loogeduser Id
    if request.user.is_authenticated():
        username = request.user.username
        userId = User.objects.get(username=username).pk

    postRev= PostReview.objects.filter(post_id = post_id,user_id =userId,review =0).count()

    if postRev == 0:
        ps = PostReview(post_id=post_id, user_id=userId,review =0)
        ps.save()

    else:
        pd = PostReview.objects.filter(post_id = post_id,user_id =userId,review =0)
        pd.delete()

    #count and discounts

    countLike = 0
    countDislike = 0

    countLike = PostReview.objects.filter(post_id = post_id,user_id =userId,review =1).count()

    countDislike = PostReview.objects.filter(post_id = post_id,user_id =userId,review =0).count()

    #all Likes and dislikes
    allLikes = PostReview.objects.filter(post_id = post_id,review =1).count()
    DisLikes = PostReview.objects.filter(post_id = post_id,review =0).count()
    if(DisLikes == 10):
        posDel = Post.objects.filter(id = post_id)
        posDel.delete()

    data = {
        'AllLikes':allLikes,
        'AllDisLikes':DisLikes,
        'countLikes':countLike,
        'countDislikes':countDislike,
        }

    return JsonResponse(data,safe=False)





def login_view(request):
	if request.method == 'POST':
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
		#login the user
			user = form.get_user()
			login(request,user)
			return redirect ("/social_Blog/home/")

	else:
		form=AuthenticationForm()
	return render(request,"login.html",{"form":form})






#	title = "Login"
#   form = UserLoginForm(request.Post or None)
#	if form.is_valid():
	#	username = form.cleaned_data.get("username")
		#password = form.cleaned_data.get('password')

#	return render(request,"form.html",{"form":form, "title":title})



def register_view(request):
	print(request.user.is_authenticated())
	title = "Register"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()

		new_user = authenticate(username = user.username , password= password)
		login(request , new_user)




	context = {"form":form ,
	"title":title}

	return render(request,"form.html",context)



def logout_view(request):
	logout(request)
	return render(request,"logout.html")
