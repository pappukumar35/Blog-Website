from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_created']
    list_filter = ['date_created', 'author']
    search_fields = ['title', 'content']
