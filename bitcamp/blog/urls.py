from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>', views.posts, name='post-detail'),
]
