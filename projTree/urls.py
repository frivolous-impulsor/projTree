"""
URL configuration for projTree project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from post import views as post_views
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('seed/', include('seed.urls')),
    path('', post_views.PostListView.as_view(), name='posts'),
    path('posts/<username>', post_views.UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>', post_views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', post_views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', post_views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', post_views.PostDeleteView.as_view(), name='post_delete'),
    path('register/', users_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', users_views.UserLogout, name='logout'),
    path('profile/', users_views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
