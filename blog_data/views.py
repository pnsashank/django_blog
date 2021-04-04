from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from blog_data.models import Blog, ImageEmbed, VideoEmbed, GithubEmbed
from blog_data.serializers import BlogSerializer, ImageEmbedSerializer, VideoEmbedSerializer, UserSerializer, GithubEmbedSerializer



class BlogPostDetails(APIView):
    """list and create details of BlogPost"""

    def get(self, request, user_id):
        """
        Return blog posts by user id

        """
        blog_posts = Blog.objects.filter(created_by=user_id)

        if not blog_posts:
            return Response ({"No blog posts availabe for user"}, status=status.HTTP_404_NOT_FOUND)

        blog_data_list = []

        for blog_object in blog_posts:
            blog_data_list.append(BlogSerializer(blog_object).data)


        return Response({'blog_data': blog_data_list}, status=status.HTTP_200_OK)


    def post(self, request):
        """
        create blog post by user id

        """
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            blog = serializer.save()
            return Response({"sucess": "Blog created '{}'!!".format(blog.name)}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        


class CreateListImageEmbed(APIView):
    """create and list ImageEmbed for the blog post"""

    def get(self, request, blog_id):
        """
        Return blog posts by user id

        """
        images = ImageEmbed.objects.filter(blog=blog_id)

        if not images:
            return Response ({"No images available for blog post"}, status=status.HTTP_404_NOT_FOUND)

        image_data_list = []

        for image_object in images:
            image_data_list.append(ImageEmbedSerializer(image_object).data)


        return Response({'image_data': image_data_list}, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Save ImageEmbed for the blog post id

        """
        serializer = ImageEmbedSerializer(data=request.data)
        if serializer.is_valid():
            image_embed= serializer.save()
            return Response({"success": "Image '{}' added to Blog '{}' successfully!!!".format(image_embed.name, image_embed.blog.id)}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class CreateListVideoEmbed(APIView):
    """create and list VideoEmbed details for the blog post"""

    def get(self, request, blog_id):
        """
        Return blog posts by user id

        """
        videos = VideoEmbed.objects.filter(blog=blog_id)

        if not videos:
            return Response ({"No videos available for blog post"}, status=status.HTTP_404_NOT_FOUND)

        videos_data_list = []

        for video_object in videos:
            videos_data_list.append(VideoEmbedSerializer(video_object).data)

        return Response({'video_data': videos_data_list}, status=status.HTTP_200_OK)

    

    def post(self, request):
        """
        Save VideoEmbed for the blog post id

        """

        serializer = VideoEmbedSerializer(data=request.data)
        if serializer.is_valid():
            video_embed = serializer.save()    
            return Response({"success": "VideoEmbed '{}' added to Blog '{}' successfully!!!".format(video_embed.name, video_embed.blog.id)}, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        

class CreateListGitHubEmbed(APIView):
    """saves VideoEmbed for the blog post"""

    def get(self, request, blog_id):
        """
        Return blog posts by user id

        """
        github_embeds = GithubEmbed.objects.filter(blog=blog_id)

        if not github_embeds:
            return Response ({"No github embeds available for blog post"}, status=status.HTTP_404_NOT_FOUND)

        github_embed_data_list = []

        for github_embed_object in github_embeds:
            github_embed_data_list.append(GithubEmbedSerializer(github_embed_object).data)

        return Response({'github_data': github_embed_data_list}, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Save VideoEmbed for the blog post id

        """

        serializer = GitHubEmbedSerializer(data=request.data)
        if serializer.is_valid():
            github_embed = serializer.save()    
            return Response({"success": "GithubEmbed code added to Blog '{}' succesfully!!!".format(github_embed.blog.id)}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class CreateUser(APIView):
    """Create User details for the blog"""

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()    
            return Response({"success": "User '{}' with id '{}' created!!!".format(user.username, user.id)}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



        



        


        

        