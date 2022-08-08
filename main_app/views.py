from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Fish, Lure
from .forms import CaughtForm

class LureList(LoginRequiredMixin, ListView):
  model = Lure

class LureDetail(LoginRequiredMixin, DetailView):
  model = Lure

class LureUpdate(LoginRequiredMixin, UpdateView):
  model = Lure
  fields = ['name', 'color']

class LureDelete(LoginRequiredMixin, DeleteView):
  model = Luresuccess_url = '/lures/'

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def fish_index(request):
  fish = Fish.objects.filter(user=request.user)
  return render(request, 'fish/index.html', { 'fish' : fish })

@login_required
def fish_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  lures_fish_doesnt_have = Lure.objects.exclude(id__in = fish.lures.all().values_list('id'))
  caught_form = CaughtForm()
  return render(request, 'fish/detail.html', { 'fish': fish, 'caught_form': caught_form, 'lures': lures_fish_doesnt_have })

class FishCreate(LoginRequiredMixin, CreateView):
  model = Fish
  fields = ['name', 'scientific_name', 'category', 'picture']
  success_url = '/fish/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class FishUpdate(LoginRequiredMixin, UpdateView):
  model = Fish
  fields = ['scientific_name', 'category', 'picture']
  success_url = '/fish/'

class FishDelete(LoginRequiredMixin, DeleteView):
  model = Fish
  success_url = '/fish/'

@login_required
def add_catch(request, fish_id):
  form = CaughtForm(request.POST)
  if form.is_valid():
    new_catch = form.save(commit=False)
    new_catch.fish_id = fish_id
    new_catch.save()
  return redirect('fish_detail', fish_id=fish_id)

class LureCreate(LoginRequiredMixin, CreateView):
  model = Lure
  fields = '__all__'

@login_required
def assoc_lure(request, fish_id, lure_id):
  Fish.objects.get(id=fish_id).lures.add(lure_id)
  return redirect('fish_detail', fish_id=fish_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('fish_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)