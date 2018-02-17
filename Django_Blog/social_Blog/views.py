from django.shortcuts import render,get_object_or_404
from .models import Post,Comment,PostReview,ForbiddenWords,ReplyComment
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Category
from .forms import CommentForm,ReplyForm
from django.contrib import messages
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers

# Create your views here.
def home (request):
	#return HttpResponse("<h1>Home Page</h1>")
	all_Catagories=Category.objects.all()
	context={"all_Catagories":all_Catagories}
	return render(request,"home.html",context)

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
    
