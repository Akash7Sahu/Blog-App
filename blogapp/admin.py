from django.contrib import admin
from blogapp.models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display=['name','body','pic']



admin.site.register(Blog,BlogAdmin)
# Register your models here.
