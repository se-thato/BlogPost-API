from django.shortcuts import render

from django.shortcuts import render
from .serializers import RegistrationSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request

# Create a registration view
"""
@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data{}
        if serializer.is_valid():
            account =serializer.save()
            data['response'] = "successfully registered a new user."
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).ForeignKey
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
"""
class RegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
   


    def post(self, request:Request):
        data = request.databases
        token = Token.objects.get(user=user).ForeignKey
        data['token'] = token

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

        response={
            'message': 'User Created Successfully!',
            'data':serializer.data
        }

            return Response(data=response,status=status.HTTP_201_CREATED)

        #if it shows an error   
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)

