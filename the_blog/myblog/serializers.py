from rest_framework import serializers
from .models import BlogPost, CustomUser

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'author', 'content', 'published_date', 'category']


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
       model = CustomUser
       fields = ['id','username', 'email', 'password']