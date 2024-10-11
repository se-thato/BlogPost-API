from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length= 200)
    title_tag = models.CharField(max_length= 200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.TextField(default='General')

    def __str__(self): 
        return self.title + '|' + str(self.author) 

    #redirecting to which page should it go
    def get_absolute_url(self):
       # return reverse('article-details', args=(str(self.id)))
       return reverse('home')

