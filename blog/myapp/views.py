from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SignUpForm, LoginForm, Addposts, ContactsForm, CommentForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def home(request):
    posts = Addpost.objects.all().order_by('-date')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 4)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'data': data})


def dashboard(request):
    data = Addpost.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'data': data})


def add_post(request):
    if request.method == 'POST':
        form = Addposts(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            messages.success(request, 'CONGRAT SUCESSFULLY SIGNUP!!')
            a = form.save()
            a.user = request.user
            a.save()
            return redirect('dashboard')
        else:
            messages.error(request, 'INVALID DATA!!')
            return redirect('addpost')
    else:
        form = Addposts()
        return render(request, 'addpost.html', {'form': form})


def contact(request):
    data = Contact.objects.all()
    return render(request, 'contacts.html', {'data': data})


def add_contact(request):
    if request.method == 'POST':
        data = ContactsForm(request.POST)
        print(data)
        if data.is_valid():
            messages.success(request, 'CONGRAT SUCESSFULLY SIGNUP!!')
            b = data.save()
            return redirect('contacts')
        else:
            messages.error(request, 'INVALID DATA!!')
            return redirect('addcontact')
    else:
        data = ContactsForm()
        return render(request, 'addcontact.html', {'data': data})


def loginn(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            us = authenticate(request, username=username, password=password)
            if us is not None:
                login(request, us)
                return redirect('home')
        else:
            pass
        f = LoginForm()
        return render(request, 'login.html', {'form': f})
    else:
        return HttpResponseRedirect('/login/')


def logoutt(request):
    logout(request)
    messages.info(request, 'LOGOUT SUCCESSFULLY!!')
    return HttpResponseRedirect('/login/')


def signupp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def deletes(request, pk):
    uid = Addpost.objects.get(id=pk)
    uid.delete()
    return HttpResponseRedirect('/dashboard/')


def likeBlog(request, pk):
    blog = Addpost.objects.get(id=pk)
    blog.like += 1
    blog.save()
    return redirect('/')


def editt(request, pk):
    blog = Addpost.objects.get(id=pk)
    post = Addposts(instance=blog)
    if request.method == 'POST':
        post1 = Addposts(request.POST, instance=blog)
        print(post1)
        if post1.is_valid():
            post1.save()
            return redirect('dashboard')
        else:
            return redirect('edit1')
    else:
        return render(request, 'edit1.html', {'post': post})


def titledetail(request, pk):
    blog = Addpost.objects.get(id=pk)
    post = Addposts(instance=blog)
    data = Comment.objects.filter(title__title=blog.title)
    # data = Comment.objects.all()
    if request.method == 'POST':
        post1 = Addposts(request.POST, instance=blog)
        print(post1)
        if post1.is_valid():
            post1.save()
            return redirect('dashboard')
        else:
            return redirect('title')
    else:
        return render(request, 'title.html', {'post': post, 'data': data})


def userdetails(request, pk):
    # detail = Contact.objects.get(user__id=pk)
    detail = Contact.objects.filter(user__id=pk).first()
    data = ContactsForm(instance=detail)
    if request.method == 'POST':
        data1 = ContactsForm(request.POST, instance=detail)
    else:
        return render(request, 'userdetails.html', {'data': data, })


def comments(request):
    # data = Comment.objects.filter(user=request.user)
    data = Comment.objects.all().order_by('-comment')
    return render(request, 'comments.html', {'data': data})


def addcomment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            a = form.save()
            a.user = request.user
            a.save()
            return redirect('comments')
        else:
            return redirect('addcomment')
    else:
        form = CommentForm()
        return render(request, 'addcomment.html', {'form': form})
