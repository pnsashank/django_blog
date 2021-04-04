from django.urls import include, path
from blog_data.views import BlogPostDetails, CreateListImageEmbed, CreateListVideoEmbed, CreateListGitHubEmbed, CreateUser

urlpatterns = [
    path('api/v1/blog/', BlogPostDetails.as_view(), name='blog_details_post'),
    path('api/v1/blog/<int:user_id>/', BlogPostDetails.as_view(), name='blog_details_get'),
    path('api/v1/blog/image/', CreateListImageEmbed.as_view(), name='blog_image_post'),
    path('api/v1/blog/image/<int:blog_id>/', CreateListImageEmbed.as_view(), name='blog_image_get'),
    path('api/v1/blog/video/', CreateListVideoEmbed.as_view(), name='blog_video_post'),
    path('api/v1/blog/video/<int:blog_id>', CreateListVideoEmbed.as_view(), name='blog_video_get'),
    path('api/v1/blog/github/', CreateListGitHubEmbed.as_view(), name='blog_video_post'),
    path('api/v1/blog/github/<int:blog_id>', CreateListGitHubEmbed.as_view(), name='blog_video_get'),
    path('api/v1/user/', CreateUser.as_view(), name='user_create')
    
]