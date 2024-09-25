from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length= 100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.TextField(default='General')

    def __str__(self): 
        return self.title   
    

class CustomUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=100)
    
    def __str__(self): 
        return self.username