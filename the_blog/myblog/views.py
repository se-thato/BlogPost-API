from django.shortcuts import render
from rest_framework import generics, status, filters
from rest_framework.response import Response
from .models import BlogPost, CustomUser
from .serializers import BlogPostSerializer, CustomUserSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    #creating search feature
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content', 'author', 'category']
    #creating pagination
    pagination_class = PageNumberPagination


    #creating an endpoint
    @api_view(['GET', 'POST'])
    def blogpost_list(request):

        #get all the available blogposts
        #serialize them
        #return json 
        if request.method == 'GET':
            blogpost = BlogPost.objects.all()
            serializer = BlogPostSerializer(blogpost, many=True)
            return Response(serializer.data)
        
        if request.method == 'POST':
            serializer = BlogPostSerializer(data=request.data)
            #check if the data sent is  valid
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)



    @api_view(['GET', 'PUT', 'DELETE'])
    def blogpost_detail(request, id):

        try:
            blogpost = BlogPost.objects.get(pk=id)
        except BlogPost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = BlogPostSerializer(blogpost)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = BlogPostSerializer(blogpost, data= request.data)
            if serializer.is_valid():
                serializer.save

        elif request.method == 'DELETE':
            blogpost.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


    #creating the delete button on my blogpost list create page
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'


class CustomUserListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def delete(self, request, *args, **kwargs):
        CustomUser.objects.all().delete()
        return Response(status=status.HHTP_204_NO_CONTENT)
    

class CustomUserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()                                     
    serializer_class = CustomUserSerializer   
    lookup_field = 'pk'                       



