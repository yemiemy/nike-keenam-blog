from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings 
from django.urls import reverse
from .models import Post, Comment, Category, Message
from .forms import commentForm, messageForm
from django.core.paginator import Paginator
# Create your views here.

def home(request):
	posts = Post.objects.order_by('-id')
	feature = Post.objects.filter(featured=True)
	paginator = Paginator(posts, 1)
	page = request.GET.get('page')
	posts = paginator.get_page(page)

	return render(request, 'index.html', {'post':posts, 'feature':feature})


def lifestyle(request):
	lifestyle = Post.objects.filter(lifestyle=True)
	return render(request, 'lifestyle.html', {'lifestyle':lifestyle})

def fashion(request):
	fashion = Post.objects.filter(fashion=True)
	return render(request, 'fashion.html', {'fashion':fashion})

def food(request):
	food = Post.objects.filter(food=True)
	return render(request, 'food.html', {'food':food})

def about(request):
	return render(request, 'about.html', {})

def contact(request):

	if request.method == 'POST':

		form = messageForm(request.POST or None)
		message1 = request.POST['email']
		message = request.POST['body']
		if form.is_valid():
			form.save()
			form = messageForm()
		send_mail('Contact Form : {}'.format(message1),
			message,
			settings.EMAIL_HOST_USER,
			['rasholayemi@gmail.com'],
			fail_silently=False)
	else:
		form = messageForm()
    
	return render(request, 'contact.html', {'form':form})

def single(request, id):
	posts = Post.objects.get(id=id)

	form = commentForm(request.POST or None)
	comments = posts.comments.all()
	
	if form.is_valid():

		comment = form.save(commit=False)
		form = commentForm()
		comment.post = posts
		comment.author = request.user
		comment.save()


	return render(request, 'single.html', {'object':posts, 'form':form, 'comments':comments}) 


def like_view(request, id):
	posts = Post.objects.get(id=id)
	user = request.user
	#user = posts.likes.all()
	
	if user in posts.likes.all():
		posts.likes.remove(user)
	else:
		posts.likes.add(user)


	#return render(request, 'details.html', {'topic': topic})
	return redirect(reverse('single', args=[id]))

def field_view(request, id):
	post = Post.objects.get(id=id)
	return redirect(reverse('single', args=[id]))


def search_view(request):
	query = request.GET['query']
	posts = Post.objects.filter(title__icontains=query)|Post.objects.filter(body__icontains=query)
	feature = Post.objects.filter(featured = True)

	return render(request, 'search.html', {'post':posts, 'query':query, 'feature':feature})

