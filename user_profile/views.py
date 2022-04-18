from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User

from .models import UserProfile
from .serializers import UserProfileSerializer, UserSerializer

# Create your views here.

# List/Create user profiles 
class UserProfileList(generics.ListCreateAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


# List create users 
class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

