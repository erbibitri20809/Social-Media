from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='media/')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Photo by {self.user}'


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.user}: {self.content}'


class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ImageField(upload_to='story/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


