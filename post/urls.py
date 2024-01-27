from django.contrib import admin
from django.urls import path, include
from post import views as post_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('posts/', post_views.PostListView.as_view(), name='posts'),
    path('posts/<username>/', post_views.UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', post_views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', post_views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', post_views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', post_views.PostDeleteView.as_view(), name='post_delete'),
]
