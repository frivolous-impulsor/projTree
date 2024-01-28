from django.urls import path
from .views import StepListView, StepCreateView, StepUpdateView, StepDeleteView

urlpatterns = [
    path('<seedName>/steps/', StepListView.as_view(), name='step_list'),
    path('<seedName>/create/', StepCreateView.as_view(), name='step_create'),
    path('<seedName>/<int:pk>/update/', StepUpdateView.as_view(), name='step_update'),
    path('<seedName>/<int:pk>/delete/', StepDeleteView.as_view(), name='step_delete'),
]