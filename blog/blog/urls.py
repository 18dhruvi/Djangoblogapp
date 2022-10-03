"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
# from myapp.admin import blog_site 
app_name = "myapp"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('add/',views.addBlog,name='addblog'),
    path('like/<str:pk>',views.likeBlog,name='like'),
    path('contacts/', views.contact, name='contacts'),
    path('comments/', views.comments, name='comments'),
    path('title/<int:pk>', views.titledetail, name='title'),
    path('userdetails/<int:pk>', views.userdetails, name='userdetails'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.loginn, name='login'),
    path('signup/', views.signupp, name='signup'),
    path('logout/', views.logoutt, name='logout'),
    path('delete/<int:pk>', views.deletes, name='delete'),
    path('addpost/', views.add_post, name='addpost'),
    path('addcontact/', views.add_contact, name='addcontact'),
    path('addcomment/', views.addcomment, name='addcomment'),
    path('edit/<int:pk>', views.editt, name='edit'),
    path('allimage/<int:pk>', views.allimage, name='allimage'),
]+ static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
