from rest_framework import serializers
from .models import Topic, Discussion, Comment

# Model serializers
class TopicSerializer(serializers.ModelSerializer):

    user = serializers.CharField(source='user.username')

    class Meta:

        model = Topic 

        fields = ['title', 'date_created', 'user']


class DiscussionSerializer(serializers.ModelSerializer):

    topic = serializers.CharField(source='topic.title')
    user = serializers.CharField(source='user.username')

    class Meta:

        model = Discussion

        fields = ['title', 'content', 'date_created', 'user', 'topic']


class CommentSerializer(serializers.ModelSerializer):

    discussion = serializers.CharField(source='discussion.title')
    user = serializers.CharField(source='user.username')

    class Meta:

        model = Comment

        fields = ['content', 'date_created', 'user', 'discussion']