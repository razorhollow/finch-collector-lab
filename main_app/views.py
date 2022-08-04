from django.shortcuts import render
from django.http import HttpResponse

class Fish:
  def __init__(self, name, description, category):
    self.name = name
    self.description = description
    self.category = category

fish = [
  Fish('Largemouth Bass', 'my pointless description of what a largemouth bass is', 'fresh water')
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def fish_index(request):
  return render(request, 'fish/index.html', { 'fish' : fish })