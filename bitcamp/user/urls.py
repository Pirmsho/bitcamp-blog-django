from django.urls import path
from .views import *



app_name='user'
urlpatterns = [
    path('login/', my_login, name='login'),
    path('logout/', logout_view, name='logout'),

    path('', AutorListView.as_view(), name='authors'),
    # path('new/', CreateAuthorView.as_view(), name='create_author'),
    path('neww/', register, name='register'),
    path('<int:pk>/', AuthorDetailView.as_view(), name='author'),
    path('<int:pk>/update/', UpdateAuthorView.as_view(), name='author_update'),
    path('<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
]