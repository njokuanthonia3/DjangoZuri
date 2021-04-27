from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class CommentInline(admin.TabularInline): # new
    model = Comment
class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline,
]

admin. site.register(Post)
admin. site.register(Comment)
