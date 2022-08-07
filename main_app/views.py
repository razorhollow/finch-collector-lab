from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def fish_index(request):
  fish = Fish.objects.filter()
  return render(request, 'fish/index.html', { 'fish' : fish })

def fish_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  return render(request, 'fish/detail.html', { 'fish': fish })

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