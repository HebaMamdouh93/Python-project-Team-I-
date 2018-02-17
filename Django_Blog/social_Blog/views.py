from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Category ,Post
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
