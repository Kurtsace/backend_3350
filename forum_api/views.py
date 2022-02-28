from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import generics

from .serializers import TopicSerializer, DiscussionSerializer, CommentSerializer
from .models import Topic, Discussion, Comment

# Create your views here.

# List of all the topics 
class TopicList(generics.ListCreateAPIView):

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

# List of all the Discussions within a Topic 
class DiscussionList(generics.ListCreateAPIView):

    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

# List of all the Comments within a Discussion
class CommentsList(generics.ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer