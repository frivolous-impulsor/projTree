from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Step
from seed.models import Seed
from django.urls import reverse

# Create your views here.
class StepListView(ListView):
    model = Step
    template_name = 'step_list.html'
    context_object_name = 'steps'
    def get_queryset(self) -> QuerySet[Any]:
        target_seed = get_object_or_404(Seed, seedName = self.kwargs.get('seedName'))
        return Step.objects.filter(seed = target_seed)