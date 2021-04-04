from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    """Create model for the blog"""
    BLOG_TYPES = (
        ('C', 'CELEBRITY'),
        ('S', 'SCIENCE'),
        ('E', 'ENGINEERING'),
        ('T', 'TRAVEL'),
        ('H', 'HEALTH'),
        ('B', 'BOOKS'),
        ('G', 'GAMES'),
        ('M', 'MOVIES'),
    )
    name = models.CharField(max_length=30, null=False, blank=False)
    text = models.TextField(max_length=200, null=False, blank=False) 
    blog_type = models.CharField(max_length=1, choices=BLOG_TYPES, null=False, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    date_added = models.DateField(auto_now_add=True)


class ImageEmbed(models.Model):
    """Create ImageEmbed for blogs"""
    name = models.CharField(max_length=30, null=False, blank=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    url = models.URLField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name

class VideoEmbed(models.Model):
    """Create VideoEmbed for blogs"""
    name = models.CharField(max_length=30, null=False, blank=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    url = models.URLField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class GithubEmbed(models.Model):
    """Create GithubEmbed for blogs"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    github = models.URLField(max_length=200, null=False, blank=False)
    date_added = models.DateField(auto_now_add=True)



