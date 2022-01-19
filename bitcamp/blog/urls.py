from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name="posts"),
    path('post/<int:pk>', views.post, name='post_detail'),
    path('comment/<int:pk>/', views.comment_detail, name='comment_detail'),
    path('comments/', views.comment_list, name='comment_list'),
]
