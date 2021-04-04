from django.contrib import admin
from .models import Blog, ImageEmbed, VideoEmbed, GithubEmbed


"""To View models on the admin site"""
admin.site.register(Blog)
admin.site.register(ImageEmbed)
admin.site.register(VideoEmbed)
admin.site.register(GithubEmbed)