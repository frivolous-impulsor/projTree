from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Seed, Step

# Create your views here.
class SeedsListView(ListView):
    model = Seed
    context_object_name = 'seeds'
    template_name = 'seed_list.html'

class SeedDetailView(DetailView):
    model = Seed
    context_object_name = 'seed'

