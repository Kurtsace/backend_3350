from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User

# User profile serializer
class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserProfile

        fields = ['user', 'bio']

    def create(self, validated_data):

        user_profile, complete = UserProfile.objects.get_or_create(**validated_data)
        return user_profile

# User serializer
class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ['id', 'username', 'password', 'email']
        write_only_fields = ['password']
        read_only_fields = ['id']
        ordering = ['id']

    def create(self, validated_data):

        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user