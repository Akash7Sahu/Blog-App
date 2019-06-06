
from django.shortcuts import render
from blogapp.forms import Signupform,Blogform
from blogapp.models import Blog
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.


def index(request):
	return render(request,'blogapp/index.html')


@login_required
def signup(request):
	form=Signupform()
	mydict={'myform':form}
	if request.method=='POST':
		form=Signupform(request.POST)
		form.save();
		print('Data Inserted In Database...')
	return render(request,'blogapp/signup.html',context=mydict)

@login_required
def post(request):
	if request.method=='POST':
		img=BlogForm(request.POST, request.FILES)
		if img.is_valid():
			data=img.save(commit=False)
			data.author=request.user
			data.save()
			return HttpResponseRedirect(reverse('post'))
	else:
		img=BlogForm()
		images=Blog.objects.all().order_by('upload_date')
		return render(request,'blogapp/postform.html',{'form':img,'images':images})

def viewblog(request):
	bloglist=Blog.objects.all()
	mydict={'viewlist':bloglist}
	return render(request,'blogapp/viewform.html',context=mydict)

@login_required
def log(request):
	form=Loginform()
	mydict={'loginform':form}
	if request.method=='POST':
		form=Loginform(request.POST)
		form.save();
		print('Data Inserted In Database...')
	return render(request,'blogapp/loginform.html',context=mydict)
