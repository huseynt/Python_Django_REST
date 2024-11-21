from django.urls import path
from .views import get_user
from .views import post_user

urlpatterns = [
    path('users/', get_user, name='get_user'),
    path('postusers/', post_user, name='post_user')
]