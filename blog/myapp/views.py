from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SignUpForm, LoginForm, Addposts, ContactsForm, CommentForm, ImageForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from django.core.mail import send_mail
from myapp.tasks import send_mail_func
import celery
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
# from django.urls import reverse


# Create your views here.
class Home(generic.ListView):
    model = Addpost
    paginate_by = 5
    template_name = 'home.html'
    context_object_name = "data"

    def get_queryset(self):
        return self.model.objects.all().order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context["all_image"] = Image.objects.all()
        return context

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(Home, self).form_valid(form)


class Contacts(generic.ListView):
    model = Contact
    template_name = 'contacts.html'
    context_object_name = "data"

    def get_queryset(self):
        self.request.user
        return self.model.objects.all().order_by('-date')


class Dashboard(generic.ListView):
    model = Addpost
    template_name = 'dashboard.html'
    context_object_name = "data"

    def get_queryset(self):
        self.request.user
        return self.model.objects.filter(user=self.request.user)


class AddpostCreateView(generic.CreateView):
    template_name = 'addpost.html'
    form_class = Addposts
    queryset = Addpost.objects.all()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddpostCreateView, self).form_valid(form)


class AddcontactCreateView(generic.CreateView):
    template_name = 'addcontact.html'
    form_class = ContactsForm
    queryset = Contact.objects.all()


class EdittView(generic.UpdateView):
    model = Addpost
    template_name = 'edit.html'
    fields = [
        'title',
        'desc',
        'date'
    ]
    success_url = reverse_lazy('dashboard')


# class LoginPageView(generic.View):
#     template_name = 'login.html'
#     form_class = LoginForm

#     def get(self, request):
#         form = self.form_class()

#         return render(request, self.template_name, context={'form': form})

#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#         return render(request, self.template_name, context={'form': form})


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


# def logoutt(request):
#     logout(request)
#     messages.info(request, 'LOGOUT SUCCESSFULLY!!')
#     return HttpResponseRedirect('/login/')

class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login/')


# def signupp(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             send_mail_func.apply_async(args=[user.email])
#             # print(send_mail_func)
#             # subject = 'Welcome to Blog application '
#             # message = f'Hi {user.username}, Thank you for register.'
#             # email_from = settings.EMAIL_HOST_USER
#             # recipient_list = [user.email, ]
#             # send_mail(subject, message, email_from, recipient_list)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class TitleDetailView(generic.DetailView):
    model = Addpost
    template_name = 'title.html'
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        instance = self.get_object()
        all_image = Image.objects.filter(addpost=instance)
        context = super().get_context_data(**kwargs)
        post = Addposts(instance=instance)
        data = Comment.objects.filter(title__title=instance.title)

        context['post'] = post
        context['data'] = data
        context['all_image'] = all_image
        return context


class UserdetailsDetailView(generic.DetailView):
    model = Contact
    template_name = 'userdetails.html'
    context_object_name = "data"


class Comments(generic.ListView):
    model = Comment
    template_name = 'comments.html'
    context_object_name = "data"

    def get_queryset(self):
        return self.model.objects.all().order_by('-comment')


class AddcommentCreateView(generic.CreateView):
    template_name = 'addcomment.html'
    form_class = CommentForm
    queryset = Comment.objects.all()

    def from_valid(self, form):
        self.request.user
        print(form.cleaned_data)
        return super().from_valid(form)

def allimage(request, pk):
    images = Image.objects.filter(addpost__pk=pk)
    return render(request, 'allimage.html', {'images': images})

class Allimage(generic.TemplateView):
	template_name = 'allimage.html'

	def get_context_data(self, *args, **kwargs):
		context = super(Allimage, self).get_context_data(*args, **kwargs)
		context['image'] = Image.objects.filter(addpost__pk=pk)
		return context


# class AllimageDetailView(generic.DetailView):
#     model = Image
#     context_object_name = 'images'
#     template_name = 'allimage.html'

#     def get_context_data(self, **kwargs):
#         image = Image.objects.filter(addpost__pk=pk)


def deletes(request, pk):
    uid = Addpost.objects.get(id=pk)
    uid.delete()
    return HttpResponseRedirect('/dashboard/')


# class deleteDeleteView(generic.DeleteView):
#     template_name = "delete.html"
    
#     def get_object(self):
#         id_ = self.kwargs.get('id')
#         return get_object_or_404(Addpost, id=id_)

def likeBlog(request, pk):
    blog = Addpost.objects.get(id=pk)
    blog.like += 1
    blog.save()
    return redirect('/')
