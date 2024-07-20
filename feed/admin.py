from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'description', )
    search_fields = ('user__username', 'description')


admin.site.register(Post, PostAdmin)
