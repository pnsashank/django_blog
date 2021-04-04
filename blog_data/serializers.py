from django.contrib.auth.models import User
from rest_framework import serializers
from blog_data.models import Blog, VideoEmbed, ImageEmbed, GithubEmbed

class BlogSerializer(serializers.ModelSerializer):
    """To serialize data in the Blog Model"""
    class Meta:
        model = Blog
        fields = '__all__'
    
    def create(self, validated_data):
        print("Creating data")
        return Blog.objects.create(**validated_data)
    
class UserSerializer(serializers.ModelSerializer):
    """serializer to create user"""
    class Meta:
        model = User
        fields = ('username', 'password')
 
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class ImageEmbedSerializer(serializers.ModelSerializer):
    """serializer to store image_embed for the blog id"""
    class Meta:
        model = ImageEmbed
        fields = '__all__'

    def create(self, validated_data):
        return ImageEmbed.objects.create(**validated_data)


class VideoEmbedSerializer(serializers.ModelSerializer):
    """serializer to store video_embed for the blog id"""
    class Meta:
        model = VideoEmbed
        fields = '__all__'

    def create(self, validated_data):
        return VideoEmbed.objects.create(**validated_data)


class GithubEmbedSerializer(serializers.ModelSerializer):
    """serializer to stire github_embed for the blog id"""
    class Meta:
        model = GithubEmbed
        fields = '__all__'

    def create(self, validated_data):
        return GithubEmbed.objects.create(**validated_data)


    

