from django.contrib import admin
from myapp.models import Addpost,Contact,Comment,Image

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
@admin.register(Addpost)
class AddpostAdmin(admin.ModelAdmin):
    list_display = ("title","desc","date","user","like")
    list_display_links = ['title']
    inlines = [CommentInline]
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("user","fname","lname","country","date")
    # list_editable = ['fname','lname','country','date']
    
@admin.register(Comment)  
class CommentAdmin(admin.ModelAdmin):
    # list_display = ['short_comment']
    list_display = ("user","title","short_comment")

admin.site.register(Image)  
