from django.db import models
from django.contrib.auth.models import User

# Create your models here.



# Topic model
class Topic(models.Model):

    # Fields 
    title = models.CharField(max_length=255, unique=True, blank=False, null=False)

    date_created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Discussion model 
class Discussion(models.Model):

    # Fields
    title = models.CharField(max_length=255, unique=True, blank=False, null=False)

    content = models.TextField(max_length=4000, blank=False, null=False)

    date_created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Comment model 
class Comment(models.Model):

    # Fields
    content = models.TextField(max_length=4000, blank=False, null=False)

    date_created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)