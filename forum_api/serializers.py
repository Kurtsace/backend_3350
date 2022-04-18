from rest_framework import serializers
from .models import Topic, Discussion, Comment

# Model serializers
class TopicSerializer(serializers.ModelSerializer):

    class Meta:

        model = Topic

        fields = ['title', 'date_created', 'user']

    def create(self, validated_data):
        topic, created = Topic.objects.get_or_create(**validated_data)
        return topic


class DiscussionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Discussion

        fields = ['title', 'content', 'date_created', 'user', 'topic']

    def create(self, validated_data):
        topic, created = Discussion.objects.get_or_create(**validated_data)
        return topic


class CommentSerializer(serializers.ModelSerializer):


    class Meta:

        model = Comment

        fields = ['content', 'date_created', 'user', 'discussion']

    def create(self, validated_data):
        topic, created = Comment.objects.get_or_create(**validated_data)
        return topic