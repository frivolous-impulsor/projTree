from django.urls import path
from .views import SeedsListView, SeedDetailView, SeedCreateView, SeedUpdateView,SeedDeleteView, UserPostedSeeds

urlpatterns = [
    path('', SeedsListView.as_view(), name='seed_list'),
    path('<int:pk>/', SeedDetailView.as_view(), name='seed_detail'),
    path('create/', SeedCreateView.as_view(), name='seed_create'),
    path('<int:pk>/update/', SeedUpdateView.as_view(), name='seed_update'),
    path('<int:pk>/delete/', SeedDeleteView.as_view(), name='seed_delete'),
    path('seeds/<username>', UserPostedSeeds.as_view(), name='user_seeds'),
]