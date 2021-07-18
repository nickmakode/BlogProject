from django.contrib import admin

# Register your models here.
from .models import blog

class adminblog(admin.ModelAdmin):
    list_display=['author','title','created_at','updated_at']
   
admin.site.register(blog,adminblog)