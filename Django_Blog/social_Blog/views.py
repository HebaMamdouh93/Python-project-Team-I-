from django.shortcuts import render,get_object_or_404,HttpResponse ,redirect
from .models import Post,Comment,PostReview,ForbiddenWords,ReplyComment ,Category ,Tag, PostTag ,User,UserCat
from django.http import HttpResponseRedirect,request,HttpResponse ,JsonResponse
from .forms import CommentForm,ReplyForm ,createPost, categoryForm, tagForm, wordForm ,userForm ,edituserForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.core.urlresolvers import reverse

from django.conf import settings
from django.core.mail import send_mail


from django.contrib.auth import(authenticate,get_user_model,login,logout,)
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserLoginForm , UserRegisterForm
from django.contrib.auth import login , authenticate
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from itertools import chain
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



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
            messages.success(request, "Successfully Edited post", extra_tags='')
            return HttpResponseRedirect(reverse('posts'))
    return render(request, 'editpost.html', {'form': form, 'tags': tags, 'list': list})


def delete(request, postId):
    post = Post.objects.get(id=postId)
    post.delete()
    messages.success(request, "Successfully Deleted Post", extra_tags='')
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
            messages.success(request, "Successfully Created new post", extra_tags='')
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
            messages.success(request, "Successfully Created  new Category", extra_tags='')
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
            messages.success(request, "Successfully created new Tag", extra_tags='')
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
            messages.success(request, "Successfully Edited word", extra_tags='')
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
            messages.success(request, "Successfully created new user", extra_tags='')
            return HttpResponseRedirect(reverse('users'))
    return render(request, 'adduser.html', {'form': form})

def deleteuser(request ,userId):
    user = User.objects.get(id=userId)
    user.delete()
    messages.success(request, "Successfully Deleted user", extra_tags='')
    return HttpResponseRedirect(reverse('users'))

def edituser(request ,userId):
    user = get_object_or_404(User, id=userId)
    if request.method == "POST":
        form = edituserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Edited user", extra_tags='')
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

    current_user = request.user.id
    checkUsersubscribe=[]
    checkUsersubscribeQuery=UserCat.objects.filter(user_id=current_user)

    for check in checkUsersubscribeQuery:
        checkUsersubscribe.append(check.cat_id)

    all_Catagories=Category.objects.all()
    all_Posts=Post.objects.all()
    latest_Posts=Post.objects.all().order_by('-publish_date')
    latest_Post=Post.objects.all().order_by('-publish_date')[:1].get()
    postsID=[]
    all_Tags=[]
    query=request.GET.get("search")
    if query:
        latest_Posts=all_Posts.filter(title__icontains=query)
        all_Tags=Tag.objects.all().filter(tagName__icontains=query)
        if(all_Tags):
        
            for tag in all_Tags:
                qResult=PostTag.objects.all().filter(tag_id=tag.id)
                postsID.append(qResult)

            for post in postsID[0]:
                qResult=all_Posts.filter(id=post.post_id)
                latest_Posts = latest_Posts | qResult 
               


    page = request.GET.get('page', 4)

    paginator = Paginator(latest_Posts,5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(4)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    context={"all_Catagories":all_Catagories ,
    "checkUsersubscribe":checkUsersubscribe ,
    "latest_Posts":latest_Posts,
    "all_Posts":all_Posts,
    "all_Tags":all_Tags,
    "posts":posts,
    "postsID":postsID,
    "latest_Post":latest_Post}
    return render(request,"home.html",context)




def showCatPosts(request,cat_id):
    #return HttpResponse("<h1>showCatPosts</h1>")
    current_user = request.user.id
     #print current_user
    checkUsersubscribe=UserCat.objects.filter(user_id=current_user)
    cat_name=Category.objects.get(id=cat_id).name
    all_Catagories=Category.objects.all()
    latest_Posts=Post.objects.filter(cat_id=cat_id).order_by('-publish_date')
    latest_Post=Post.objects.filter(cat_id=cat_id).order_by('-publish_date')[:1].get()
    context={"all_Catagories":all_Catagories ,
    "checkUsersubscribe":checkUsersubscribe,
    "latest_Posts":latest_Posts,
    "latest_Post":latest_Post,
    "cat_name":cat_name}
    return render(request,"CatPosts.html",context)



############## Subscribe with Ajax ###########################
@csrf_exempt
def subscribe(request):

    userID = request.POST.get('userID', None)
    catID = request.POST.get('catID', None)
    catName = request.POST.get('catName', None)
    UserCat.objects.create(cat_id=catID, user_id=userID)
    subject="Confirmation email from django"
    message="you successfully subscribed in "+catName+" category all posts related to this category will display on your home page "
    emailFrom=settings.EMAIL_HOST_USER
    emailTo=[request.user.email]
    send_mail(subject, message, emailFrom,emailTo,fail_silently=True)
    data = {
        'success': True
    }
    return JsonResponse(data)

############## unSubscribe with Ajax ###########################
@csrf_exempt
def unsubscribe(request):
    
    userID = request.POST.get('userID', None)
    catID = request.POST.get('catID', None)
    #UserCat.objects.create(cat_id=catID, user_id=userID)
    UserCat.objects.filter(cat_id=catID, user_id=userID).delete()
    data = {
        'success': True
    }
    return JsonResponse(data)

############## Subscribe with Ajax ###########################
@csrf_exempt
def subscribe(request):

    userID = request.POST.get('userID', None)
    catID = request.POST.get('catID', None)
    catName = request.POST.get('catName', None)
    UserCat.objects.create(cat_id=catID, user_id=userID)
    subject="Confirmation email from django"
    message="you successfully subscribed in "+catName+" category all posts related to this category will display on your home page "
    emailFrom=settings.EMAIL_HOST_USER
    emailTo=[request.user.email]
    send_mail(subject, message, emailFrom,emailTo,fail_silently=True)
    data = {
        'success': True
    }
    return JsonResponse(data)

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
            if request.user.is_active:
                return redirect ("/social_Blog/home/")

    else:
        form=AuthenticationForm()
    return render(request,"login.html",{"form":form})


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
        return redirect ("/social_Blog/home/")

    context = {"form":form ,
    "title":title}
    return render(request,"form.html",context)





def logout_view(request):
    logout(request)
    return redirect ("/social_Blog/home/")
    return render(request,"logout.html")
