from django.urls import path
from .views import SeedsListView, SeedDetailView, SeedCreateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', SeedsListView.as_view(), name='seed_list'),
    path('<int:pk>/', SeedDetailView.as_view(), name='seed_detail'),
    path('create/', SeedCreateView.as_view(), name='seed_form'),
]