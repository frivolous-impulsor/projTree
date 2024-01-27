from django.urls import path
from .views import StepListView

urlpatterns = [
    path('<seedName>/', StepListView.as_view(), name='seed_steps'),
]