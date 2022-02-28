from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# User profile model 
class UserProfile(models.Model):

    # Fields 
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField(max_length=2000, blank=False, null=False)

    def __str__(self):
        return str(self.user)