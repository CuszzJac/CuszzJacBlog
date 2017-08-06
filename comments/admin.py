from django.contrib import admin

# Register your models here.
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'created_time', 'name', 'text']


admin.site.register(Comment, CommentAdmin)
