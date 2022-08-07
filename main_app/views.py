from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Fish, Lure
from .forms import CaughtForm

class LureList(ListView):
  model = Lure

class LureDetail(DetailView):
  model = Lure

class LureUpdate(UpdateView):
  model = Lure
  fields = ['name', 'color']

class LureDelete(DeleteView):
  model = Luresuccess_url = '/lures/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def fish_index(request):
  fish = Fish.objects.filter()
  return render(request, 'fish/index.html', { 'fish' : fish })

def fish_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  caught_form = CaughtForm()
  return render(request, 'fish/detail.html', { 'fish': fish, 'caught_form': caught_form })

class FishCreate(CreateView):
  model = Fish
  fields = ['name', 'scientific_name', 'category', 'picture']
  success_url = '/fish/'

class FishUpdate(UpdateView):
  model = Fish
  fields = ['scientific_name', 'category', 'picture']
  success_url = '/fish/'

class FishDelete(DeleteView):
  model = Fish
  success_url = '/fish/'

def add_catch(request, fish_id):
  form = CaughtForm(request.POST)
  if form.is_valid():
    new_catch = form.save(commit=False)
    new_catch.fish_id = fish_id
    new_catch.save()
  return redirect('fish_detail', fish_id=fish_id)

class LureCreate(CreateView):
  model = Lure
  fields = '__all__'