from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# Create your views here.

def free_board(request):
    categorys = Category.objects.filter(name = "자유게시판")
    post = Community_Post.objects.filter(category__name = "자유게시판")
    context = {
        'post':post,
        'categorys' : categorys,
    }
    return render(request, 'free_board.html', context)

def review_board(request):
    categorys = Category.objects.filter(name = "경기 후기")
    post = Community_Post.objects.filter(category__name = "경기 후기")
    context = {
        'post':post,
        'categorys' : categorys,
    }
    return render(request, 'review_board.html', context)


def hire_board(request):
    categorys = Category.objects.filter(name = "용병 모집")
    post = Community_Post.objects.filter(category__name =  "용병 모집")
    context = {
        'post':post,
        'categorys' : categorys,
    }
    return render(request, 'hire_board.html', context)

def createPost_free(request):
    if request.method == "POST":
        form = Community_Form(request.POST)
        if form.is_valid():
            #author = Profile.objects.get(user__username=request.user)
            authod_id = request.session.get('user')
            user = Users.objects.get(pk = authod_id)

            new_Post = Community_Post(
                    title = form.cleaned_data['title'],
                    title_image = form.cleaned_data['title_image'],
                    content = form.cleaned_data['content'],
                    author = user,
                    category = get_object_or_404(Category, pk = id),
            )
            new_Post.save()
            return redirect('/')

    else:
        form = Community_Form()
        context = {
            'form' : form,
        }
        return render(request, 'createPost.html', context)

def createPost_review(request):
    if request.method == "POST":
        form = Community_Form(request.POST)
        if form.is_valid():
            #author = Profile.objects.get(user__username=request.user)
            authod_id = request.session.get('user')
            user = Users.objects.get(pk = authod_id)

            new_Post = Community_Post(
                    title = form.cleaned_data['title'],
                    title_image = form.cleaned_data['title_image'],
                    content = form.cleaned_data['content'],
                    author = user,
                    category = get_object_or_404(Category, pk = id),
            )
            new_Post.save()
            return redirect('/')

    else:
        form = Community_Form()
        context = {
            'form' : form,
        }
        return render(request, 'createPost.html', context)

def createPost_hire(request):
    if request.method == "POST":
        form = Community_Form(request.POST)
        if form.is_valid():
            #author = Profile.objects.get(user__username=request.user)
            authod_id = request.session.get('user')
            user = Users.objects.get(pk = authod_id)

            new_Post = Community_Post(
                    title = form.cleaned_data['title'],
                    title_image = form.cleaned_data['title_image'],
                    content = form.cleaned_data['content'],
                    author = user,
                    category = get_object_or_404(Category, pk = id),
            )
            new_Post.save()
            return redirect('/')

    else:
        form = Community_Form()
        context = {
            'form' : form,
        }
        return render(request, 'createPost.html', context)
    
def postDetail(request, id):
    post = get_object_or_404(Community_Post, pk = id)
    context = {
        'post' : post,
    }
    return render(request, 'postDetail.html', context)