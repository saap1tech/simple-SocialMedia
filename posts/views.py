from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from .forms import *
from .models import *

@login_required(login_url='/login/')
def home(request):
    form = PostForm()
    text = request.POST.get('text')
    image = request.FILES.get('image')
    if text and image:
        model = Post()
        model.text = text
        model.user = request.user
        model.image = image
        model.save()

    elif text:
        model = Post()
        model.text = text
        model.user = request.user
        model.save()

    show = Post.objects.all()

    context = {
        "form": form,
        "show": show,
    }

    return render(request, 'home1.html', context)

@login_required(login_url='/login/')
def add(request, id):
    post = Post.objects.get(id=id)

    like = request.POST.get('like')

    if like:
        like1 = Like()
        like1.user = request.user
        like1.post = post.id
        like1.save()

    nlike = Like.objects.filter(user=request.user, post=id)

    likes = Like.objects.filter(post=id).count()

    if likes:
        show_likes = likes
    else:
        show_likes = 0

    text = request.POST.get("text")

    if text:
        comment1 = Comment()
        comment1.user = request.user
        comment1.post = post.id
        comment1.comment = text
        comment1.save()

    show_comments = Comment.objects.filter(post=id)

    context = {
        "show": post,
        "value": nlike,
        "likes": show_likes,
        "comments": show_comments,
    }
    return render(request, 'add.html', context)

@login_required(login_url='/login/')
def profile(request):

    form = PostForm()
    text = request.POST.get('text')
    image = request.FILES.get('image')
    if text and image:
        model = Post()
        model.text = text
        model.user = request.user
        model.image = image
        model.save()

    elif text:
        model = Post()
        model.text = text
        model.user = request.user
        model.save()

    show = Post.objects.filter(user=request.user)

    context = {
        'form': form,
        'show': show
    }

    return render(request, 'index.html', context)