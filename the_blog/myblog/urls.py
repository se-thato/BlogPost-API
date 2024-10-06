from django.urls import path
from . import views


urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost-create'),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name= 'update'),
    path('user/', views.CustomUserListCreate.as_view(), name='custom-user'),
    path('user/<int:pk>/', views.CustomUserRetrieveUpdateDestroy.as_view(), name= 'update-user'),
    
]

