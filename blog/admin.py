from django.contrib import admin

from blog.models import Comment, Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'text']
    raw_id_fields = ('post', 'author')
    search_fields = ['author__username', 'post__title', 'text']


admin.site.register(Tag)
