from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Step
from seed.models import Seed
from django.urls import reverse, reverse_lazy
from seed.models import Seed

# Create your views here.
class StepListView(ListView):
    model = Step
    template_name = 'step_list.html'
    context_object_name = 'steps'
    def get_queryset(self) -> QuerySet[Any]:
        target_seed = get_object_or_404(Seed, seedName = self.kwargs.get('seedName'))
        return Step.objects.filter(seed = target_seed)
    
class StepCreateView(LoginRequiredMixin, CreateView):
    model = Step
    fields = ['img', 'title', 'content']
    def form_valid(self, form):
        target_seedName = self.kwargs['seedName']
        seed = Seed.objects.get(seedName = target_seedName)
        form.instance.seed = seed
        return super().form_valid(form)
    def get_success_url(self):
        # Pass seedName to get_absolute_url
        return self.object.get_absolute_url(seedName=self.kwargs['seedName'])

class StepUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Step
    fields = ['img', 'title', 'content']
    def test_func(self) -> bool | None: #ensure current user only edits their posts
        step = self.get_object()
        return step.seed.author == self.request.user
    
    def get_success_url(self):
        # Pass seedName to get_absolute_url
        return self.object.get_absolute_url(seedName=self.kwargs['seedName'])
    
class StepDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Step
    def get_success_url(self):
        # Pass seedName to get_absolute_url
        return self.object.get_absolute_url(seedName=self.kwargs['seedName'])
    def test_func(self) -> bool | None: #ensure current user only edits their posts
        step = self.get_object()
        return step.seed.author == self.request.user