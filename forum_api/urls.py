from django.urls import path
from .views import TopicList, DiscussionList, CommentsList

app_name = 'forum_api'

urlpatterns = [
    path('topics/', TopicList.as_view(), name='topic_list'),
    path('discussions/', DiscussionList.as_view(), name='discussion_list'),
    path('comments/', CommentsList.as_view(), name='comments_list')
]