from django.urls import path
from .views import SeedsListView, SeedDetailView

urlpatterns = [
    path('', SeedsListView.as_view(), name='seed_list.html'),
    path('<int:pk>/', SeedDetailView.as_view(), name='seed_detail.html'),
]
