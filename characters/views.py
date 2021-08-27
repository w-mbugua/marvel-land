from django.shortcuts import render
from django.http import HttpResponse
from .req import get_heroes

# Create your views here.
def home(request):
  characters = get_heroes()
  return render(request, 'home.html', {'characters': characters})

