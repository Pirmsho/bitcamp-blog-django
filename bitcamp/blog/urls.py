from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    # path('posts/', posts, name="posts"),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>', post, name='post'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('post/new/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('comment/<int:pk>/', comment_detail, name='comment_detail'),
    # path('comment_create/', comment_create, name='comment_create'),
    path('createcomment/', CommentCreateView.as_view(), name='createcomment'),
    path('comments/', comment_list, name='comment_list'),

    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category'),

]
