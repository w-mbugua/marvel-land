from django.shortcuts import render
from django.http import HttpResponse
from .req import get_characters

# Create your views here.
def home(request):
  characters = get_characters()
  return render(request, 'home.html', {'characters': characters})

