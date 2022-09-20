from django.contrib import admin
from myapp.models import Addpost,Contact,Comment

# Register your models here.
@admin.register(Addpost)
class AddpostAdmin(admin.ModelAdmin):
    list_display = ("title","desc","date","user")
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("user","fname","lname","country","subject")
    
admin.site.register(Comment)  