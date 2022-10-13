from django.contrib import admin
from myapp.models import Addpost,Contact,Comment,Image
# from admin_auto_filters.filters import AutocompleteFilter
# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment

# class AddpostFilter(AutocompleteFilter):
#     title = 'Addpost' # display title
#     field_name = 'user' # name of the foreign key field

# @admin.register(Addpost)
class AddpostAdmin(admin.ModelAdmin):
    model = Addpost
    list_display = ("title","desc","date","user","like")
    search_fields = ['title','user__username' ]
    # list_display_links = ['title']
    # inlines = [CommentInline]
    
admin.site.register(Addpost, AddpostAdmin)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("user","fname","lname","country","date")
    
@admin.register(Comment)  
class CommentAdmin(admin.ModelAdmin):
    # list_display = ['short_comment']
    list_display = ("user","title","short_comment")

admin.site.register(Image)  

