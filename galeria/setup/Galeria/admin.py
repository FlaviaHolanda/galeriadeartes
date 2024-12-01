from django.contrib import admin

from .models import Comment, Image

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "image"]




class CommentAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Comment, CommentAdmin)

admin.site.register(Image, ImageAdmin)