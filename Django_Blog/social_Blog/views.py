from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Category
# Create your views here.
def home (request):
	#return HttpResponse("<h1>Home Page</h1>")
	all_Catagories=Category.objects.all()
	context={"all_Catagories":all_Catagories}
	return render(request,"home.html",context)
