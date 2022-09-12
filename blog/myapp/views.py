from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SignUpForm, LoginForm, UserChangeForm, Addposts
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.


def home(request):
    posts = Addpost.objects.all()
    return render(request, 'home.html', {'posts': posts})


def contacts(request):
    if request.method == 'POST':
        Contact.objects.create(fname=request.POST['fname'],
                               lname=request.POST['lname'],
                               country=request.POST['country'],
                               subject=request.POST['subject'])
        messages.success(request, 'MESSAGE SEND SUCCESSFULLY!!')
    return render(request, 'contact.html')


def dashboard(request):
    msg = 'ADDED SUCCESSFULLY!!!!'
    many = Addpost.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'many': many})


def add_post(request):
    if request.method == 'POST':
        form = Addposts(request.POST)
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


def logoutt(request):
    logout(request)
    messages.info(request, 'LOGOUT SUCCESSFULLY!!')
    return render(request, 'logout.html')


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

# def signupp(request):
#     if request.method=='POST':
#         form=SignUpForm(request.POST)
#         print(form)
#         if form.is_valid():

#             # messages.success(request,'CONGRAT SUCESSFULLY SIGNUP!!')
#             form.save()
#             return redirect('login')
#         else:
#             messages.error(request,'INVALID DATA!!')
#             return redirect('signup')
#     else:
#         form= SignUpForm()
#         return render(request,'signup.html',{'form':form})


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
    

def deletes(request, pk):
    uid = Addpost.objects.get(id=pk)
    uid.delete()
    return HttpResponseRedirect('/dashboard/')


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
