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
from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
# from myapp.admin import blog_site 
app_name = "myapp"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.Home.as_view(), name='home'),
    # path('add/',views.addBlog,name='addblog'),
    path('like/<str:pk>',views.likeBlog,name='like'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('comments/', views.Comments.as_view(), name='comments'),
    path('title/<int:pk>', views.TitleDetailView.as_view(), name='title'),
    path('userdetails/<int:pk>', views.UserdetailsDetailView.as_view(), name='userdetails'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    # path('login/', views.LoginPageView.as_view(), name='login'),
    path('login/', views.loginn, name='login'),
    # path('signup/', views.signupp, name='signup'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # path('delete/<int:pk>', views.deletes, name='delete'),
    path('addpost/', views.AddpostCreateView.as_view(), name='addpost'),
    path('addcontact/', views.AddcontactCreateView.as_view(), name='addcontact'),
    path('addcomment/', views.AddcommentCreateView.as_view(), name='addcomment'),
    path('edit/<int:pk>/', views.EdittView.as_view(), name='edit'),
    path('allimage/<int:pk>', views.Allimage.as_view(), name='allimage'),
    path('<int:pk>/delete/', views.Deletes.as_view(), name='delete'),
]+ static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
