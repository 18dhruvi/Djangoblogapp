from django.contrib import admin
from myapp.models import Addpost,Contact,Comment

# Register your models here.

@admin.register(Addpost)
class AddpostAdmin(admin.ModelAdmin):
    list_display = ("image","title","desc","date","user","like")
    list_display_links = ['title']
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("user","fname","lname","country","subject")
    list_editable = ['fname','lname','country','subject']
    
@admin.register(Comment)  
class CommentAdmin(admin.ModelAdmin):
    list_display = ['short_comment']
    # list_display = ("user","title","comment")
