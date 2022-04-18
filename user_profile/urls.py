from django.urls import path
from .views import UserProfileList, UserList

app_name = 'user_profile_api'

urlpatterns = [
    path('user_profiles/', UserProfileList().as_view(), name='user_profile_list'),
    path('users/', UserList.as_view(), name='user_list')
]