from django.contrib import admin
from .models import Post, Comment, Story


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'description', 'created_at')
    search_fields = ('user__username', 'description')


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'content')
    search_fields = ('content', 'user__username', 'post__caption')


admin.site.register(Comment, CommentAdmin)


class StoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'story', 'created_at')
    search_fields = ('user__username',)


admin.site.register(Story, StoryAdmin)
