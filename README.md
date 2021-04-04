##  Installation Steps:
1. git clone https://github.com/pnsashank/django_blog.git
2. pip3 install requirements.txt

##  Link to Postman Collection:
https://www.getpostman.com/collections/f8176d1439a6182b76db 


##  About:

This Repository is for a hypothetical blogging site. The table names and columns are as follows:

1. Blog
	[
		 name: CharField,
		 text:  CharField,
		 blog_type: CharField,
		 created_by: User (Foreign Key),
		 date_added: DateField (auto_add_now),
	]
	
2. Image Embed
	[
		name: CharField,
		blog: Blog (Foreign Key),
	 	url: URLField,
	]
	
3. Video Embed
	[
		name: CharField,
		blog: Blog (Foreign Key),
		url: URLField,
	]
	
4. GitHub Embed
	[
		blog: Blog (Foreign Key),
		github: URLField,
		date_added: DateField (auto_add_now),
	]
	
5. User (Inbuilt)

Assumed Relationships between tables:

1. Each user can create multiple blogs but each blog can belong to only one user
2. Each Blog can have multiple image embed, video embed and github embeds but each image embed, video embed and github embed belong to one blog.  


## Endpoints:

```
1. POST (Create user):
http://127.0.0.1:8000/blogs/api/v1/user/

SAMPLE REQUEST:
{ 
 "username": "test_user_name",
 "password": "test_password"
 }

SAMPLE RESPONSE:
{
"success": "User 'test_user_name' with id",
'test_user_id' created !!!"
}
```
```
2. GET (Get blog posts by user id): 
http://127.0.0.1:8000/blogs/api/v1/blog/user_id

Parameters: user_id

SAMPLE RESPONSE:
{
'blog_data': '[
	{
		'name': 'test_name',
		'text': 'test_text',
		'blog_type': 'test_blog_type',
		'created_by': 'test_user_id',
	}................
]'
```
```
3. POST (Create blog post for a user id):
http://127.0.0.1:8000/blogs/api/v1/blog/

SAMPLE REQUEST:
{
		'name': 'test_name',
		'text': 'test_text',
		'blog_type': 'test_blog_type',
		'created_by': 'test_user_id',
}

SAMPLE RESPONSE:
{
"success": "Blog text_blog_name created !!"
}
```
```
4. GET (Get all images for az blog id):
http://127.0.0.1:8000/blogs/api/v1/blog/image/blog_id

Parameters: blog_id

SAMPLE RESPONSE:
{
'image_data': '[
	{
		'name': 'test_name',
		'blog': 'blog_id',
		'url': 'image_url_link',	
   }................
]'
```
```
5. POST (Create image for a blog id):
http://127.0.0.1:8000/blog/api/v1/image/

SAMPLE REQUEST:
{
		'name': 'test_name',
		'blog': 'blog_id',
		'url': 'test_image_url',
}

SAMPLE RESPONSE:
{
"success": "Image 'test_name' added to Blog 'blog_id' successfully !!!"
}
```
```
6. GET (Get all videos for a blog id):
http://127.0.0.1:8000/blogs/api/v1/blog/video/blog_id

Parameters: blog_id

SAMPLE RESPONSE:
{
'video_data': '[
	{
		'name': 'test_name',
		'blog': 'blog_id',
		'url': 'video_url_link',	
   }................
]'

```
```
7. POST (Create video for a blog id):
http://127.0.0.1:8000/blogs/api/v1/blog/video/

SAMPLE REQUEST:
{
		'name': 'test_name',
		'blog': 'blog_id',
		'url': 'test_video_url',
}

SAMPLE RESPONSE:
{
"success": "VideoEmbed 'test_name' added to Blog 'blog_id' successfully !!!"
}
```
```
8. GET (Get all the githug code for a blog id):
http://127.0.0.1:8000/blogs/api/v1/blog/github/blog_id

Parameters: blog_id

SAMPLE RESPONSE:
{
'github_data': '[
	{
		'blog': 'blog_id',
		'github': 'github_url_link',	
   }................
]'
```
```
9. POST (Create github code for a blog id):
http://127.0.0.1:8000/blogs/api/v1/blog/github/

SAMPLE REQUEST:
{
		'blog': 'blog_id',
		'github': 'test_github_url',
}

SAMPLE RESPONSE:
{
"success": "GitHubEmbed code added to Blog 'blog_id' successfully !!!"
}
```

## Notes:

1. Assumption can be made to have many to many relationship between image embed , video embed and Blog.

2. Urls for image, video and github have been chosen so that the UI can render image from the url.

3. SQLite test database is also added (I understand its a bad practice) but it might make it easier for the endpoints to be tested.
